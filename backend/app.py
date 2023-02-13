from flask import Flask, request, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_migrate import Migrate
from decouple import config
import os
import shortuuid
import time

app = Flask(__name__)
USERNAME=config('username')
PASSWORD=config('password')
DATABASE=config('database')

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{USERNAME}:{PASSWORD}@localhost:5432/{DATABASE}"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class UsersModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(22), primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)

    children = relationship("EventsModel")

    # Encode password later
    def __init__(self, email, password):
        self.id=shortuuid.uuid()
        self.email=email
        self.password=password

    def __repr__(self):
        return f"<User {self.email}>"

class EventsModel(db.Model):
    __tablename__ = 'events'

    # Differentiate Event_id from User_id better later, e.g. Event_id is BASED off User_id.
    id = db.Column(db.String(22), primary_key=True)
    event = db.Column(db.String(150))
    user_id = db.Column(db.String(22), db.ForeignKey("users.id"))

    def __init__(self, event, user_id):
        self.id=shortuuid.uuid()
        self.event=event
        self.user_id=user_id

    def __repr__(self):
        return f"<Event {self.event}>"


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

# Integrated HTTP error messages for easier debugging
@app.route('/users/generate', methods=['POST'])
def generate_user():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()

            # Check if email is already inside database due constraint of every email being unique
            exists = bool(UsersModel.query.filter_by(email=data['email']).first())
            if exists:
                return make_response({"error": "A user with this email address already exists"}, 409)
            else:
                new_user = UsersModel(email=data['email'], password=data['password'])
                db.session.add(new_user)
                db.session.commit()

                success_message = {"message": f"user {new_user.email} with id={new_user.id} has been created successfully"}
                return make_response(success_message, 201)
        else:
            return make_response({"error": "The request payload is not JSON Format"}, 400)
    else:
        return make_response({"error": "Method not allowed"}, 400)

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

@app.route('/events', methods=['GET'])
def view_events():
    if request.method == 'GET':
        events = EventsModel.query.all()
        results = [
            {
                "id": unique_event.id,
                "event": unique_event.event
            } for unique_event in events
        ]
        return {"count": len(results), "events": results}
    else:
        return {"error": "Method not allowed" }

@app.route('/events/add/', methods=['POST'])
def generate_event():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_event = EventsModel(event=data['event'], user_id=data['user_id'])
            db.session.add(new_event)
            db.session.commit()
            return {"message": f"event={new_event.event} for user with id={new_event.user_id} has been created successfully"}
        else:
            return {"error": "The request payload is not JSON Format"}
    else:
        return {"error": "Method not allowed" }






# Time API imported from Python to show time on the front-end sign-in page
@app.route('/time')
def get_current_time():
    return {'time': time.ctime(int(time.time()))}

@app.route('/test')
def test_return():
    return {'test': "test"}

if __name__ == '__main__':
    app.run(port="5000", debug=True)


