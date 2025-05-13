from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

ADMIN_IDS = [7264453091]
tasks = []
notifications = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return "<h1>Панель управления</h1><p>Функции администратора загружены.</p>"

@app.route("/api/check_user", methods=["POST"])
def check_user():
    data = request.get_json()
    user_id = int(data.get("id", 0))
    return jsonify({"ok": user_id in ADMIN_IDS})

if __name__ == "__main__":
    app.run(debug=True)