import datetime
import sqlite3
from flask import Flask, app, render_template, request, redirect, url_for
from flask_login import LoginManager, login_required, login_user

from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id):
        self.id = id

app = Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key_here'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    username = request.form.get('username')
    password = request.form.get('password')

    with sqlite3.connect('app.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM User WHERE UserName=? and PassWord=? ', (username, password))
        is_authentificated = True if len(cursor.fetchall()) == 1 else False

    if is_authentificated:
        user = User(username)
        login_user(user)
        return redirect(url_for('top'))

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    
    with sqlite3.connect('app.db') as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO User VALUES(?, ?, ?)', (request.form.get('username'), request.form.get('password'), datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")))

    return redirect(url_for('login'))

@app.route('/top', methods=['GET', 'POST'])
@login_required
def top():
    return render_template('top.html')

if __name__ == "__main__":
    app.run(debug=True)