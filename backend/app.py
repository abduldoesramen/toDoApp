from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from decouple import config
import os
import shortuuid

app = Flask(__name__)
USERNAME=config('username')
PASSWORD=config('password')
DATABASE=config('database')

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{USERNAME}:{PASSWORD}@localhost:5432/{DATABASE}"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class UsersModel(db.Model):
    __tablename__ = 'users'

    # Edit specifics later, i.e. id must be 22 characters, email must be unique, both email&pass must exist, etc.
    id = db.Column(db.String(22), primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))

    # Encode password later
    def __init__(self, email, password):
        self.id=shortuuid.uuid()
        self.email=email
        self.password=password

    def __repr__(self):
        return f"<Car {self.email}>"


@app.route('/users', methods=['POST', 'GET'])
def handle_users():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_user = UsersModel(email=data['email'], password=data['password'])
            db.session.add(new_user)
            db.session.commit()
            return {"message": f"user {new_user.email} has been created successfully."}
        else:
            return {"error:" "The request payload is not JSON Format"}
    elif request.method == 'GET':
        users = UsersModel.query.all()
        results = [
            {
                "id": user.id,
                "email": user.email
            } for user in users
        ]
        return {"count": len(results), "cars": results}


# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy 
# from sqlalchemy import create_engine
# import os
# from dotenv import load_dotenv
# import psycopg2
# import shortuuid

# load_dotenv()

# # PostgreSQL Database credentials loaded from the .env file
# username=os.getenv('username')
# password=os.getenv('password')
# database=os.getenv('database')

# db = SQLAlchemy()

# def create_app():
#     app = Flask(__name__)
#     app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{username}:{password}@localhost/{database}"
#     db.init_app(app)

#     db.app=app
#     with app.test_request_context():
#         db.create_all()
    
#     from .views import main
#     app.register_blueprint(main)


#     return app
    # conn_string = f"host='localhost' dbname='{database}' user='{username}' password='{password}'"





# from flask import Flask, jsonify, request
# from flask_cors import CORS
# import psycopg2
# import os
# from dotenv import load_dotenv
# import shortuuid
# import time
# import harperdb

# load_dotenv()

# # PostgreSQL Database credentials loaded from the .env file
# username=os.getenv('username')
# password=os.getenv('password')
# database=os.getenv('database')

# # HarperDB Database credentials loaded from the .env file
# # harperdb_url = os.getenv('harperdb_url')
# # harperdb_username = os.getenv('harperdb_username')
# # harperdb_password = os.getenv('harperdb_password')

# app = Flask(__name__)

# # Match information for our cloud database (HarperDb in this case)
# # db = harperdb.HarperDB(
# #     url=harperdb_url,
# #     username=harperdb_username,
# #     password=harperdb_password
# # )

# CORS(app)

# try: 
#     # Attempt and set up connection and cursor in local postgres server
#     conn = psycopg2.connect(f"postgresql://{username}:{password}@localhost:5432/{database}")
#     cur = conn.cursor()

#     # GET: Fetch all the current users from the local postgres database
#     @app.route('/', methods=['GET'])
#     def fetch_all_users():
#         cur.execute("SELECT * from users;")
#         records = cur.fetchall()

#         # Need to return this to tuple to the frontend
#         print(records)
#         return jsonify(records)

#     # GET: Fetch user by Email from database via URL
#     @app.route('/<string:email>', methods=['GET'])
#     def fetch_user_by_email(email=None):
#         cur.execute(f"""
#         SELECT * from users
#         WHERE email='{email}'
#         """
#         )
#         records = cur.fetchall()
#         print(records)

#         return jsonify(records)

#     # DELETE: Delete a user by their Email from local postgres database
#     @app.route('/delete/<string:email>', methods=['GET', 'DELETE'])
#     def delete_user_by_email(email=None):
#         cur.execute(f"""
#         DELETE FROM users
#         WHERE email='{email}'
#         RETURNING UserId
#         """
#         )
#         conn.commit()
#         return f'User with Email: {email} has been deleted.'
    
#     # POST: Add user to local postgres database via Postman via Body Parameters
#     @app.route('/add-user', methods=['GET', 'POST'])
#     def add_new_user():
#         if request.method == 'POST':
#             data = request.args.to_dict()
#             print(data)
#             cur.execute("INSERT INTO users (UserId, email, password) VALUES (%s, %s, %s)",
#             (f"{shortuuid.uuid()}", f"{data['emailValue']}", f"{data['passwordValue']}")
#             )
#             conn.commit()
#             return 'Form submitted'
#         else:
#             return 'Form submission failed'

#     # HarperDB test routes
#     # Note: currently, HarperDB is its own database - need to learn how to connect Postgres with HarperDb

#     # GET: Fetch all the current users from HarperDb cloud database
#     @app.route('/harperdb')
#     def harperdb_fetch_all():
#         fetch_all = db._sql('SELECT * FROM dev.users')
#         print(fetch_all)
#         return jsonify(fetch_all)

#     # POST: Add user to HarperDb cloud database via Postman via Body Parameters
#     @app.route('/harperdb/add-user', methods=['GET', 'POST'])
#     def harperdb_add_user():
#         if request.method == 'POST':
#             data = request.args.to_dict()
#             print(data)

#             (f"{shortuuid.uuid()}", f"{data['email']}", f"{data['password']}")
#             add_new_user = db._sql(
#                 f"INSERT INTO dev.users(UserId, email, password) VALUES ('{shortuuid.uuid()}', '{data['email']}', '{data['password']}')" 
#             )
#             print(add_new_user)
#             return 'Form submitted'
#         else:
#             return 'Form submission failed'

#     # Time API imported from Python to show time on the front-end sign-in page
#     @app.route('/time')
#     def get_current_time():
#         return {'time': time.ctime(int(time.time()))}
    
#     # Close cursor and connection once testing is done (avoid 'this block is still running')
#     # cur.close()
#     # conn.close()
# except:
#     print('Error')

# if __name__ == '__main__':
#     app.run(port="5000")
