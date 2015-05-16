from flask import Flask, flash, redirect, url_for, request, get_flashed_messages, render_template, session
from flask.ext.login import LoginManager, current_user, login_user, logout_user, login_required
from models import *
import rlcompleter, pdb


app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.secret_key = 'pcduino'

@login_manager.user_loader
def load_user(id):
    return AuthUser.get(id)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welcome')
def welcome():
    if current_user.is_authenticated():
        return render_template('welcome.html')
    else:
        flash(login_manager.login_message)
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = AuthUser.get(request.form['username'])
        if (user and user.password == request.form['password']):
            login_user(user)
            return redirect(url_for('welcome'))
        else:
            flash('Username or password incorrect')
            return render_template('login.html')
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
