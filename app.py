import datetime
import os
import sqlite3
from flask import Flask, app, render_template, request, redirect, url_for
from flask_login import LoginManager, login_required, login_user

from flask_login import UserMixin

from db.accessor.userCredentialAccessor import userCredentialAccessor
from db.data.userCredential import userCredential

class User(UserMixin):
    def __init__(self, id):
        self.id = id

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')
print(app.config['SECRET_KEY'])

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
    
    credential = userCredential(username, password)
    fetchedUser = userCredentialAccessor.getUser(credential)
    is_authentificated = True if len(fetchedUser) == 1 else False

    if is_authentificated:
        user = User(username)
        login_user(user)
        return redirect(url_for('top'))

    return render_template('login.html', canLogin="id またはパスワードが違います")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    
    with sqlite3.connect('app.db') as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO User VALUES(?, ?, ?)', (request.form.get('username'), request.form.get('password'), datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")))

    return redirect(url_for('canSignup', canSignup=True))

@app.route('/canSignup/<canSignup>/', methods=['GET', 'POST'])
def canSignup(canSignup):
    if canSignup:
        return render_template('canSignup.html', msg="登録が完了しました。")
    return render_template('canSignup.html', msg="入力された ユーザー名 は既に使われています")

@app.route('/top', methods=['GET', 'POST'])
@login_required
def top():
    return render_template('top.html')

if __name__ == "__main__":
    app.run(debug=True)