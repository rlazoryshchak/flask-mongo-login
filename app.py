from flask import *
from models import *
import rlcompleter, pdb

# pdb.Pdb.complete=rlcompleter.Completer(locals()).complete;pdb.set_trace()

app = Flask(__name__)

app.secret_key = 'pcduino'

@app.route('/')
def home():
	return 'Home'

@app.route('/welcome')
def welcome():
	return render_template('welcome.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['user'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid credentials'
		else:
			session['logged_in'] = True
			flash('You are logged in')
			return redirect(url_for('welcome'))
	return render_template('login.html', error=error)

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	return redirect(url_for('welcome'))

if __name__ == '__main__':
	app.run(debug=True)
