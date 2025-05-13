
from flask import Flask, request, redirect, render_template

app = Flask(__name__)

ADMIN_IDS = [7264453091]

@app.route('/')
def index():
    tg_id = request.args.get('id', type=int)
    return render_template("index.html", user_id=tg_id)

@app.route('/check_user')
def check_user():
    tg_id = request.args.get('id', type=int)
    if tg_id in ADMIN_IDS:
        return redirect('/admin')
    else:
        return redirect('/user')

@app.route('/admin')
def admin_panel():
    return render_template("admin.html")

@app.route('/user')
def user_panel():
    return render_template("user.html")
