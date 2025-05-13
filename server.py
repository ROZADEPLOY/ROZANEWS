
import os
from flask import Flask, request, render_template, redirect, jsonify
from telegram import Bot
from telegram.utils.request import Request

app = Flask(__name__)

# Конфигурация
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_IDS = list(map(int, os.getenv("ADMIN_IDS", "7264453091").split(",")))
USERS = {7264453091: "Админ"}
TASKS = []
ALERT = {"active": False, "level": "Нет"}
RESULTS = []

# Telegram Bot
bot = Bot(token=BOT_TOKEN, request=Request())

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
    try:
        bot.send_message(chat_id=int(request.json["user_id"]),
                         text=f"📝 Новая задача: {request.json['title']}")
    except Exception as e:
        print("Ошибка уведомления о задаче:", e)
    return jsonify(success=True)

@app.route("/api/get_tasks", methods=["POST"])
def get_tasks():
    data = request.json
    uid = int(data["user_id"])
    return jsonify([t for t in TASKS if int(t["user_id"]) == uid])

@app.route("/api/alert", methods=["POST"])
def alert():
    ALERT["active"] = True
    ALERT["level"] = request.json.get("level", "Не указан")
    # Уведомляем всех сотрудников
    for uid in USERS:
        try:
            bot.send_message(chat_id=uid, text=f"🚨 Уровень тревоги: {ALERT['level']}")
        except Exception as e:
            print("Ошибка рассылки тревоги:", e)
    return jsonify(success=True)

@app.route("/api/get_alert")
def get_alert():
    return jsonify(ALERT)

@app.route("/api/upload_result", methods=["POST"])
def upload_result():
    RESULTS.append(request.json)
    # Уведомим админа
    for aid in ADMIN_IDS:
        try:
            bot.send_message(chat_id=aid, text=f"📄 Новый отчёт от ID {request.json['user_id']}")
        except Exception as e:
            print("Ошибка уведомления об отчёте:", e)
    return jsonify(success=True)

@app.route("/api/get_results")
def get_results():
    return jsonify(RESULTS)
