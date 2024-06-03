#!/usr/bin/python3
"""
Module task_04_flask

A simple Flask API with endpoints for various functionalities.
"""


from flask import Flask, jsonify, request


app = Flask(__name__)


users = {}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data', methods=['GET'])
def get_all_usernames():
    return jsonify(list(users.keys()))

@app.route('/status', methods=['GET'])
def status():
    return "OK"

@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    username = data.get('username')

    if username in users:
        return jsonify({"error": "Username already exists"}), 400
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == '__main__':
    app.run(debug=True)
