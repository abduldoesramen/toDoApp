from flask import Blueprint, jsonify, request
from . import db
from .models import User
import shortuuid

main = Blueprint('main', __name__)

@main.route('/add_user', methods=["POST"])
def add_user():
    user_data = request.get_json()

    new_user = User(UserId = shortuuid.uuid(), email = user_data['email'], password = user_data['password'])
    db.session.add(new_user)
    db.session.commit()

    return 'Done', 201

@main.route('/users')
def users():
    
    users = []
    return jsonify({'users' : users})