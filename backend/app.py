from flask import Flask
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Env private attributes
username=os.getenv('username')
password=os.getenv('password')
database=os.getenv('database')

@app.route('/')
def index():
    print("TEST")
    conn = psycopg2.connect(f"postgresql://abdultest:{password}@localhost:5432/{database}")
    return f"hi:{os.getenv('database')}"

@app.route('/time')
def get_current_time():
    return {'time': time.ctime(int(time.time()))}

if __name__ == '__main__':
    app.run(port="5003")
