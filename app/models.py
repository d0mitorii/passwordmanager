from enum import unique
from app.database import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), nullable=False)
    login = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id


class PasswordManager(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_login = db.Column(db.String(20), db.ForeignKey(Users.login))
    source = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    login = db.Column(db.String(20), nullable=True)
    password = db.Column(db.String(8), nullable=False)

    def __repr__(self):
        return '<Item %r>' % self.id

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()