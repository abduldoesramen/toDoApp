from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

# PostgreSQL Database credentials loaded from the .env file
username=os.getenv('username')
password=os.getenv('password')
database=os.getenv('database')

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{username}:{password}@localhost:5000/todoapp"

    db.init_app(app)

    from .views import main
    app.register_blueprint(main)

    return app
    # conn_string = f"host='localhost' dbname='{database}' user='{username}' password='{password}'"