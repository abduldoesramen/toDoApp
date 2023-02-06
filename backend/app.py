from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
import os
from dotenv import load_dotenv
import shortuuid
import time

load_dotenv()

app = Flask(__name__)

# PostgreSQL Database credentials loaded from the .env file
username=os.getenv('username')
password=os.getenv('password')
database=os.getenv('database')

# HarperDB Database credentials loaded from the .env file

CORS(app)

try: 
    conn = psycopg2.connect(f"postgresql://{username}:{password}@localhost:5432/{database}")
    cur = conn.cursor()
    # GET: Fetch all the current users from the database
    @app.route('/', methods=['GET'])
    def fetch_all_users():
        cur.execute("SELECT * from users;")
        records = cur.fetchall()
        # Need to return this to tuple to the frontend
        print(records)
        return jsonify(records)

    # GET: Fetch user by Email from database
    @app.route('/<string:email>', methods=['GET'])
    def fetch_user_by_email(email=None):
        cur.execute(f"""
        SELECT * from users
        WHERE email='{email}'
        """
        )
        records = cur.fetchall()
        print(records)

        return jsonify(records)

    @app.route('/delete/<string:email>', methods=['GET', 'DELETE'])
    def delete_user_by_email(email=None):
        cur.execute(f"""
        DELETE FROM users
        WHERE email='{email}'
        RETURNING UserId
        """
        )
        conn.commit()
        return f'User with Email: {email} has been deleted.'

    # Add user via URL with username and password (CHANGE LATER)
    @app.route('/<email>/<userpassword>', methods=['GET', 'POST'])
    def add_user(email, userpassword): 
        #if request.method == 'POST':
        cur.execute('INSERT INTO users (UserId, email, password) VALUES (%s, %s, %s)',
            (shortuuid.uuid(), email, userpassword)
        )
        conn.commit()
        return 'ran'

    # Time, for displaying on Front-end
    @app.route('/time')
    def get_current_time():
        return {'time': time.ctime(int(time.time()))}
    
    # Close cursor and connection
    # cur.close()
    # conn.close()
except:
    print('Error')

if __name__ == '__main__':
    app.run(port="5000")
