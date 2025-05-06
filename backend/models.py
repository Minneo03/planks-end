from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))
    price = db.Column(db.Float)
