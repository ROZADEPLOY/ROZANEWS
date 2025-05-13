
from flask import Flask, request, render_template, redirect, jsonify
app = Flask(__name__)

ADMIN_IDS = [7264453091]
USERS = {7264453091: "Админ"}
TASKS = []
ALERT = {"active": False}
RESULTS = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check_user")
def check_user():
    tg_id = request.args.get("id", type=int)
    if tg_id in ADMIN_IDS:
        return redirect("/admin")
    elif tg_id in USERS:
        return redirect("/user")
    return render_template("unauthorized.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/user")
def user():
    return render_template("user.html")

@app.route("/api/add_user", methods=["POST"])
def add_user():
    data = request.json
    USERS[int(data["user_id"])] = data["codename"]
    return jsonify(success=True)

@app.route("/api/create_task", methods=["POST"])
def create_task():
    TASKS.append(request.json)
    return jsonify(success=True)

@app.route("/api/get_tasks", methods=["POST"])
def get_tasks():
    data = request.json
    uid = int(data["user_id"])
    return jsonify([t for t in TASKS if int(t["user_id"]) == uid])

@app.route("/api/alert", methods=["POST"])
def alert():
    ALERT["active"] = True
    return jsonify(success=True)

@app.route("/api/get_alert")
def get_alert():
    return jsonify(ALERT)

@app.route("/api/upload_result", methods=["POST"])
def upload_result():
    RESULTS.append(request.json)
    return jsonify(success=True)
