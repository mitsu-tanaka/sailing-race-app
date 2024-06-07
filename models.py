from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Race(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    participants = db.Column(db.Integer, nullable=False)
    winner = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Race(name='{self.name}', date='{self.date}', participants={self.participants}, winner='{self.winner}')"

