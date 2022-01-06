from app.database import db
from datetime import datetime


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    login = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    reg_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    def __repr__(self):
        return '<User %r>' % self.id


class UserData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(Users.id), nullable=False)
    source = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    login = db.Column(db.String(20), nullable=True)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return '<Item %r>' % self.id

    def add(self):
        db.session.add(self)
        db.session.commit()
    
    def edit(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()