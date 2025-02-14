from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///citizens.db'
app.config['SECRET_KEY'] = '3d6f45a5fc12445dbac2f59c3b6c7cb1'
db = SQLAlchemy(app)

class Citizen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    voted = db.Column(db.Boolean, default=False)

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        citizen = Citizen.query.filter_by(username=username).first()
        if citizen and check_password_hash(citizen.password, password):
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return 'Invalid username or password', 401
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        citizen = Citizen.query.filter_by(username=username).first()
        if citizen:
            return 'Username already exists', 400
        new_citizen = Citizen(username, password)
        db.session.add(new_citizen)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html')
    else:
        return redirect(url_for('login'))

@app.route('/vote', methods=['GET', 'POST'])
def vote():
    if 'username' in session:
        if request.method == 'POST':
            candidate = request.form['candidate']
            citizen = Citizen.query.filter_by(username=session['username']).first()
            if not citizen.voted:
                citizen.voted = True
                db.session.commit()
                return 'Vote cast successfully'
            else:
                return 'You have already voted', 400
        return render_template('vote.html')
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)