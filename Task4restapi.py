 from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample in-memory database
users = {
    1: {"name": "Alice", "email": "alice@example.com"},
    2: {"name": "Bob", "email": "bob@example.com"}
}

# Home route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the User API!"})


# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)


# GET single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


# POST - Add a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = max(users.keys()) + 1 if users else 1
    users[user_id] = {"name": data['name'], "email": data['email']}
    return jsonify({"message": "User added", "user": users[user_id]}), 201


# PUT - Update an existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id in users:
        data = request.get_json()
        users[user_id]["name"] = data["name"]
        users[user_id]["email"] = data["email"]
        return jsonify({"message": "User updated", "user": users[user_id]})
    return jsonify({"error": "User not found"}), 404


# DELETE - Remove a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "User deleted"})
    return jsonify({"error": "User not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)