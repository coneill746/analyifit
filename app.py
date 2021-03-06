from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = "Your_secret_string"

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return ""

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'fitness101' and request.form['username'] == 'analyifit':
        session['logged_in'] = True
        return render_template('index.html')
    else:
        flash('wrong password!')
    return home()

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')


if __name__ == "__main__":
    app.secret_key = os.urandom()
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
