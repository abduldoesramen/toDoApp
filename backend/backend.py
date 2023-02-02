import time
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import psycopg2
import os

load_dotenv()

DATABASE = os.getenv('DATABASE')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')

app = Flask(__name__)

# CORS implemented so that we don't 
# get errors when trying to access the server from a different server location
CORS(app)

try:
    con = psycopg2.connect(
        database=DATABASE,
        user=DATABASE_USERNAME,
        password=DATABASE_PASSWORD)    
        
    cur = con.cursor()  
    @app.route('/')
    def fetch_all_users():
        cur.execute('SELECT * FROM users')
        rows = cur.fetchall()
        print(rows)        
        return jsonify(rows)
except:
    print('Error')


@app.route('/time')
def get_current_time():
    return {'time': time.ctime(int(time.time()))}

if __name__ == '__main__':
    app.run(host=os.getenv("app_host"), port="5000")
