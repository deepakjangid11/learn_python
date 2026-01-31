from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import re

app = Flask(__name__)


# HARD-CODED DATABASE
users_db = [
    {
        "id": 1,
        "username": "admin",
        "email": "admin@gmail.com",
        "password": generate_password_hash("Admin@123"),
        "role": "ADMIN",
        "active": True,
        "failed_attempts": 0,
        "created_at": "2024-01-01"
    },
    {
        "id": 2,
        "username": "deepak",
        "email": "deepak@gmail.com",
        "password": generate_password_hash("Deepak@123"),
        "role": "USER",
        "active": True,
        "failed_attempts": 0,
        "created_at": "2024-02-15"
    },
    {
        "id": 3,
        "username": "guest",
        "email": "guest@gmail.com",
        "password": generate_password_hash("Guest@123"),
        "role": "GUEST",
        "active": False,
        "failed_attempts": 0,
        "created_at": "2024-03-10"
    },
    {
        "id": 4,
        "username": "pranit",
        "email": "pranit@gmail.com",
        "password": generate_password_hash("pranit@123"),
        "role": "pranit",
        "active": False,
        "failed_attempts": 0,
        "created_at": "2024-03-11"
    }
]


# LOGIN LOGS

login_logs = []

def add_log(username, status):
    login_logs.append({
        "username": username,
        "status": status,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

# VALIDATIONS
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def find_user(username, email):
    for user in users_db:
        if user["username"] == username or user["email"] == email:
            return user
    return None

# LOGIN API
@app.route("/login", methods=["POST"])
def login():
    data = request.json

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not password:
        return jsonify({"error": "Password required"}), 400

    if email and not validate_email(email):
        return jsonify({"error": "Invalid email format"}), 400

    user = find_user(username, email)

    if not user:
        add_log(username, "USER NOT FOUND")
        return jsonify({"error": "User not found"}), 404

    if not user["active"]:
        add_log(user["username"], "ACCOUNT BLOCKED")
        return jsonify({"error": "Account is blocked"}), 403

    if not check_password_hash(user["password"], password):
        user["failed_attempts"] += 1
        add_log(user["username"], "WRONG PASSWORD")

        if user["failed_attempts"] >= 3:
            user["active"] = False
            add_log(user["username"], "AUTO BLOCKED")

        return jsonify({
            "error": "Invalid password",
            "failed_attempts": user["failed_attempts"]
        }), 401

    # SUCCESS LOGIN
    user["failed_attempts"] = 0
    add_log(user["username"], "LOGIN SUCCESS")

    return jsonify({
        "message": "Login successful",
        "user": {
            "id": user["id"],
            "username": user["username"],
            "email": user["email"],
            "role": user["role"],
            "created_at": user["created_at"]
        }
    }), 200


# VIEW ALL USERS (ADMIN)
@app.route("/users", methods=["GET"])
def view_users():
    return jsonify(users_db), 200

# VIEW LOGIN LOGS
@app.route("/logs", methods=["GET"])
def view_logs():
    return jsonify(login_logs), 200

# SERVER START
if __name__ == "__main__":
    app.run(debug=True)
