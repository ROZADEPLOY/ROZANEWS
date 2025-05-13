
from flask import Flask, render_template, request, redirect
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

ADMIN_IDS = [7264453091]
employees = {7264453091: 'Капитан'}

tasks = []
alerts = []
reports = {}

@app.route('/')
def index():
    tg_id = request.args.get('id', type=int)
    return render_template('index.html', user_id=tg_id)

@app.route('/check_user')
def check_user():
    tg_id = request.args.get('id', type=int)
    if tg_id in ADMIN_IDS:
        return redirect(f'/admin?id={tg_id}')
    elif tg_id in employees:
        return redirect(f'/user?id={tg_id}')
    else:
        return "Доступ запрещён", 403

@app.route('/admin')
def admin_panel():
    tg_id = request.args.get('id', type=int)
    if tg_id not in ADMIN_IDS:
        return "Доступ запрещён", 403
    return render_template('admin.html', user_id=tg_id)

@app.route('/user')
def user_panel():
    tg_id = request.args.get('id', type=int)
    if tg_id not in employees:
        return "Доступ запрещён", 403
    user_tasks = [t for t in tasks if t['user_id'] == tg_id]
    return render_template('user.html', tasks=user_tasks, user_id=tg_id)

@app.route('/add_employee', methods=['POST'])
def add_employee():
    user_id = int(request.form['user_id'])
    callsign = request.form['callsign']
    employees[user_id] = callsign
    return redirect(f"/admin?id={request.args.get('id')}")

@app.route('/add_task', methods=['POST'])
def add_task():
    task = {
        'user_id': int(request.form['user_id']),
        'title': request.form['title'],
        'description': request.form['description']
    }
    tasks.append(task)
    return redirect(f"/admin?id={request.args.get('id')}")

@app.route('/send_alert', methods=['POST'])
def send_alert():
    alerts.append(request.form['level'])
    return redirect(f"/admin?id={request.args.get('id')}")

@app.route('/upload_report', methods=['POST'])
def upload_report():
    user_id = int(request.form['user_id'])
    file = request.files['file']
    content = file.read().decode('utf-8')
    reports[user_id] = content
    return redirect(f"/user?id={user_id}")
