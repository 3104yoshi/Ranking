import datetime
import sqlite3
from flask import Flask, app, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    with sqlite3.connect('app.db') as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO User VALUES(?, ?, ?)', (request.form.get('username'), request.form.get('password'), datetime.datetime.now().strftime("%Y/%m/%d")))

    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)