#!/usr/bin/python3
"""
Module task_05_basic_security

Ce module implémente un serveur Flask avec une authentification de base
et une authentification par token JWT. Il inclut également des points de
terminaison protégés par des rôles d'utilisateur.
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Change this to a random secret key

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Users stored in memory with hashed passwords
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    """
    Verify password for basic authentication.

    Parameters:
    - username: The username provided by the client.
    - password: The password provided by the client.

    Returns:
    - The username if authentication is successful, otherwise None.
    """
    if username in users and check_password_hash(users[username]['password'], password):
        return username

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """
    Basic Auth protected route.

    Returns:
    - A message "Basic Auth: Access Granted" if the user provides valid basic authentication credentials.
    """
    return "Basic Auth: Access Granted"

@app.route('/login', methods=['POST'])
def login():
    """
    JWT login route.

    Accepts JSON payload with username and password. Returns a JWT token if credentials are valid.

    Example Request:
    {
        "username": "user1",
        "password": "password"
    }

    Example Response:
    {
        "access_token": "<JWT_TOKEN>"
    }
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = users.get(username)
    
    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(identity={'username': username, 'role': user['role']})
        return jsonify(access_token=access_token)
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """
    JWT protected route.

    Returns:
    - A message "JWT Auth: Access Granted" if the user provides a valid JWT token.
    """
    return "JWT Auth: Access Granted"

@app.route('/admin-only')
@jwt_required()
def admin_only():
    """
    Role-based protected route.

    Returns:
    - A message "Admin Access: Granted" if the user is an admin.
    - A 403 Forbidden response if the user is not an admin.
    """
    current_user = get_jwt_identity()
    if current_user['role'] == 'admin':
        return "Admin Access: Granted"
    return jsonify({"error": "Forbidden"}), 403

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Handle unauthorized error for JWT.

    Returns:
    - A 401 Unauthorized response with an error message.
    """
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Handle invalid token error for JWT.

    Returns:
    - A 401 Unauthorized response with an error message.
    """
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    """
    Handle expired token error for JWT.

    Returns:
    - A 401 Unauthorized response with an error message.
    """
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """
    Handle revoked token error for JWT.

    Returns:
    - A 401 Unauthorized response with an error message.
    """
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """
    Handle needs fresh token error for JWT.

    Returns:
    - A 401 Unauthorized response with an error message.
    """
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == "__main__":
    app.run(debug=True)