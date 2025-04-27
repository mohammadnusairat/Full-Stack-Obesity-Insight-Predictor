from flask import Blueprint, request, jsonify
from app.database.database import get_user_collection
from app.utils.auth import create_token, verify_password, hash_password
import pymongo

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    users = get_user_collection()

    if users.find_one({'username': data['username']}):
        return jsonify({"error": "Username already exists"}), 400

    hashed_pw = hash_password(data['password'])
    users.insert_one({
        "username": data['username'],
        "password": hashed_pw
    })
    return jsonify({"message": "User registered successfully."}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    users = get_user_collection()

    user = users.find_one({'username': data['username']})
    if not user or not verify_password(data['password'], user['password']):
        return jsonify({"error": "Invalid username or password"}), 401

    token = create_token(str(user['_id']))
    return jsonify({"token": token})
