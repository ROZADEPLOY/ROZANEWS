import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
ADMIN_IDS = list(map(int, os.getenv("ADMIN_IDS", "").split(",")))

users = {}
tasks = []
alerts = []
uploads = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check_user", methods=["POST"])
def check_user():
    user_id = int(request.json.get("user_id", 0))
    if user_id in ADMIN_IDS:
        return jsonify({"role": "admin"})
    elif user_id in users:
        return jsonify({"role": "staff", "name": users[user_id]})
    return jsonify({"role": "none"}), 403

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.json
    user_id = int(data.get("id"))
    callsign = data.get("callsign")
    users[user_id] = callsign
    return jsonify({"status": "added"})

@app.route("/add_task", methods=["POST"])
def add_task():
    task = request.json
    tasks.append(task)
    return jsonify({"status": "task_added"})

@app.route("/tasks/<int:user_id>")
def get_tasks(user_id):
    return jsonify([t for t in tasks if t["user_id"] == user_id])

@app.route("/alert", methods=["POST"])
def send_alert():
    alert = request.json.get("message")
    alerts.append(alert)
    return jsonify({"status": "alert_sent"})

@app.route("/alerts")
def get_alerts():
    return jsonify(alerts)

@app.route("/upload_result", methods=["POST"])
def upload_result():
    data = request.json
    user_id = int(data["user_id"])
    result = data["result"]
    uploads.setdefault(user_id, []).append(result)
    return jsonify({"status": "received"})

@app.route("/results")
def results():
    return jsonify(uploads)
