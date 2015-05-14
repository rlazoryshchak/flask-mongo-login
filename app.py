from flask import Flask, flash, redirect, url_for, request, get_flashed_messages, render_template, session
from flask.ext.login import LoginManager, current_user, login_user, logout_user, login_required
from models import *
import rlcompleter, pdb

# pdb.Pdb.complete=rlcompleter.Completer(locals()).complete;pdb.set_trace()

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.secret_key = 'pcduino'

@login_manager.user_loader
def load_user(id):
    return User.get(id)

@app.route('/')
def home():
    return 'Home'


@app.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.get(request.form['username'])
        if (user and user.password == request.form['password']):
            login_user(user)
            return redirect(url_for('welcome'))
        else:
            flash('Username or password incorrect')
            return render_template('login.html')
    return render_template('login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=False)
