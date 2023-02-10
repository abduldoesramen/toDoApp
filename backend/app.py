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
        return f"<User {self.email}>"


@app.route('/users', methods=['GET'])
def view_users():
    if request.method == 'GET':
        users = UsersModel.query.all()
        results = [
            {
                "id": user.id,
                "email": user.email
            } for user in users
        ]
        return {"count": len(results), "users": results}
    else:
        return {"error": "Method not allowed" }

@app.route('/users/generate', methods=['POST'])
def generate_user():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_user = UsersModel(email=data['email'], password=data['password'])
            db.session.add(new_user)
            db.session.commit()
            return {"message": f"user {new_user.email} with id={new_user.id} has been created successfully"}
        else:
            return {"error": "The request payload is not JSON Format"}
    else:
        return {"error": "Method not allowed" }

@app.route('/users/<user_id>', methods=['PUT', 'DELETE'])
def edit_user(user_id):
    # Route methods for existing users inside the database only
    existing_user = UsersModel.query.get_or_404(user_id)

    if request.method == 'PUT':
        data = request.get_json()
        # Only a user's email and password are available to update
        existing_user.email = data['email']
        existing_user.password = data['password']
        db.session.add(existing_user)
        db.session.commit()
        return {"message": f"user with email={existing_user.email} has been successfully updated"}
    elif request.method == 'DELETE':
        db.session.delete(existing_user)
        db.session.commit()
        return {"message": f"user with email={existing_user.email} has been successfully deleted"}

if __name__ == '__main__':
    app.run(debug=True)


