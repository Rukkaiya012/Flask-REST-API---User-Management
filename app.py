from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
    1: {"name": "Alice", "email": "alice@example.com"},
    2: {"name": "Bob", "email": "bob@example.com"},
}

# Route to get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# Route to get a specific user
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

# Route to add a new user
@app.route('/users', methods=['POST'])
def add_user():
    print("Headers:", request.headers)
    print("Raw body:", request.data)
    
    data = request.get_json(force=True, silent=True)
    print("Parsed JSON:", data)

    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Missing data"}), 400

    new_id = max(users.keys(), default=0) + 1
    users[new_id] = {"name": data['name'], "email": data['email']}
    return jsonify({"id": new_id, "user": users[new_id]}), 201

# Route to update a user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    users[user_id].update(data)
    return jsonify({"id": user_id, "user": users[user_id]}), 200

# Route to delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        deleted_user = users.pop(user_id)
        return jsonify({"message": "User deleted", "user": deleted_user}), 200
    return jsonify({"error": "User not found"}), 404

# Root route
@app.route('/')
def home():
    return "Welcome to the User API! Try /users", 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
