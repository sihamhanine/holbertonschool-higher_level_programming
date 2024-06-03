#!/usr/bin/python3
"""
Module task_05_basic_security

Ce module implémente un serveur Flask avec une authentification de base
et une authentification par token JWT. Il inclut également des points de
terminaison protégés par des rôles d'utilisateur.
"""

import secrets
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)

app = Flask(__name__)
auth = HTTPBasicAuth()

app.config['JWT_SECRET_KEY'] = secrets.token_urlsafe(32)
jwt = JWTManager(app)

# Users stored in memory with hashed passwords
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}


@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Data route
@app.route('/data', methods=['GET'])
def get_usernames():
    return jsonify(list(users.keys()))

# Status route
@app.route('/status', methods=['GET'])
def status():
    return "OK"

# Get user by username
@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

# Add user route
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    username = data.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 400
    
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    return jsonify({"message": "User added", "user": users[username]}), 201

# Login route
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    user = users.get(username)

    if not user or not check_password_hash(user['password'], password):
        return jsonify({"error": "Invalid username or password"}), 401
    
    access_token = create_access_token(identity={"username": username, "role": user["role"]})
    return jsonify(access_token=access_token)

# Basic protected route
@app.route('/basic-protected', methods=['GET'])
def basic_protected():
    auth = request.authorization
    if not auth or not check_password_hash(users.get(auth.username, {}).get('password', ''), auth.password):
        return "Unauthorized Access", 401
    return "Basic Auth: Access Granted"

# JWT protected route
@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

# Admin only route
@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user["role"] != "admin":
        return jsonify({"error": "Forbidden"}), 403
    return "Admin Access: Granted"

if __name__ == '__main__':
    app.run(debug=True)
