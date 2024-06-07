from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/tanakamitsuru/sailing-race-app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Race(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(10), nullable=False)
    participants = db.Column(db.Integer, nullable=False)
    winner = db.Column(db.String(80), nullable=False)

@app.route('/')
def index():
    races = Race.query.all()
    return render_template('index.html', races=races)

@app.route('/add', methods=['POST'])
def add_race():
    name = request.form['name']
    date = request.form['date']
    participants = request.form['participants']
    winner = request.form['winner']
    new_race = Race(name=name, date=date, participants=int(participants), winner=winner)
    db.session.add(new_race)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
