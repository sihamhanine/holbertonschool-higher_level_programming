from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"name": "John", "age": 30, "city": "New York"}
}


@app.route('/')
def home():
    """
    Method taht return the meassge bienvenue
    """
    return "Welcome to the Flask API!"


@app.route('/data')
def get_usernames():
    """
    method that endpoint to return list of usernames
    """
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """
    method that return status
    """
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """
    Method that return user details by username
    """
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"})


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Method that add new user
    """
    user_data = request.get_json()
    username = user_data.get('username')
    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data})


if __name__ == "__main__":
    """
    method that run the server flask
    """
    app.run(debug=True)
