from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

ADMIN_IDS = [7264453091]
USERS = {}

TASKS = []
ALERT = {"active": False}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/check_user", methods=["POST"])
def check_user():
    data = request.json
    user_id = int(data.get("user_id", 0))
    if user_id in ADMIN_IDS:
        return jsonify({"role": "admin"})
    elif user_id in USERS:
        return jsonify({"role": "user", "codename": USERS[user_id]})
    else:
        return jsonify({"role": "none"})

@app.route("/api/add_user", methods=["POST"])
def add_user():
    data = request.json
    user_id = int(data["user_id"])
    codename = data["codename"]
    USERS[user_id] = codename
    return jsonify(success=True)

@app.route("/api/create_task", methods=["POST"])
def create_task():
    data = request.json
    TASKS.append(data)
    return jsonify(success=True)

@app.route("/api/get_tasks", methods=["POST"])
def get_tasks():
    user_id = int(request.json["user_id"])
    if user_id in ADMIN_IDS:
        return jsonify(TASKS)
    else:
        return jsonify([t for t in TASKS if t["user_id"] == user_id])

@app.route("/api/alert", methods=["POST"])
def alert():
    ALERT["active"] = request.json["active"]
    return jsonify(success=True)

@app.route("/api/get_alert", methods=["POST"])
def get_alert():
    return jsonify(ALERT)