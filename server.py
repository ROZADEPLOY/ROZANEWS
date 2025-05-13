import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = os.getenv("WEBAPP_URL", "https://rozawebapp.onrender.com")

raw_admin_ids = os.getenv("ADMIN_IDS", "")
ADMIN_IDS = [int(x) for x in raw_admin_ids.split(",") if x.strip().isdigit()]

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/api/check_user", methods=["POST"])
def check_user():
    data = request.json
    user_id = int(data.get("user_id", 0))
    return jsonify({
        "success": True,
        "is_admin": user_id in ADMIN_IDS
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)