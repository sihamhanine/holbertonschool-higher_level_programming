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
    """
    Welcome message endpoint

    Returns:
        str: A welcome message.
    """
    return "Welcome to the Flask API!"


@app.route('/data')
def get_usernames():
    """
    Endpoint to return list of usernames

    Returns:
        JSON: A list of usernames stored in the 'users' dictionary.
    """
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """
    Endpoint to return status

    Returns:
        str: "OK" indicating that the API is running.
    """
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """
    Endpoint to return user details by username

    Args:
        username (str): The username to retrieve.

    Returns:
        JSON: User details if the username exists, otherwise an error message.
    """
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"})


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Endpoint to add new user

    Method:
        POST

    Request Body:
        JSON: {
            "username": "str",
            "name": "str",
            "age": int,
            "city": "str"
        }

    Returns:
        JSON: Confirmation message with the added user's data.
    """
    user_data = request.get_json()
    username = user_data.get('username')
    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data})


if __name__ == "__main__":
    app.run(debug=True)
