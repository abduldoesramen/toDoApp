from flask import Flask
import psycopg2
import os
from dotenv import load_dotenv
import shortuuid
import time

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

app = Flask(__name__)

# Env private attributes
username=os.getenv('username')
password=os.getenv('password')
database=os.getenv('database')

# SQL alchemy attempt to connect to todoapp_db: 
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{username}:{password}@localhost:5432/{database}'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
# app.app_context().push()
# all_users = db.Table('users', db.metadata, autoload=True, autoload_with=db.engine)

# Array to hold all previous values
numbers = [1, 2, 3, 4, 5]

# Function to return an ordered, unique integer
ordered_number = 0
def return_random(ordered_number):
    if ordered_number not in numbers:
        return ordered_number
    else:
        ordered_number += 1
        return_random(ordered_number)

@app.route('/')
def index():
    # results = db.session.query(all_users).all()
    # for r in results:
    #     print(r.password)
    conn = psycopg2.connect(f"postgresql://{username}:{password}@localhost:5432/{database}")

    cur = conn.cursor()
    cur.execute("SELECT * from users;")
    records = cur.fetchall()
    # Need to return this to tuple to the frontend
    cur.close()
    conn.close()
    return f"hi:{os.getenv('username')} {records}"

@app.route('/<email>/<userpassword>')
def add_user(email, userpassword): 
    conn = psycopg2.connect(f"postgresql://{username}:{password}@localhost:5432/{database}")
    cur = conn.cursor()
    cur.execute('INSERT INTO users (UserId, email, password) VALUES (%s, %s, %s)',
        (shortuuid.uuid(), email, userpassword)
    )
    conn.commit()
    cur.close()
    conn.close()
    return 'ran'

@app.route('/time')
def get_current_time():
    return {'time': time.ctime(int(time.time()))}

if __name__ == '__main__':
    app.run(port="5000")
