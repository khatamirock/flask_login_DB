
from time import time
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(1000), nullable=False)
    time = db.Column(db.DateTime, default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    shared = db.Column(db.Integer, default=False)

    shared_with = db.relationship('sharedIds',
                                  backref='Note', lazy='dynamic')

    def __repr__(self):
        return '<Note %r>' % self.content


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20))
    email = db.Column(db.String(30), unique=True)
    notes = db.relationship('Note',  # this means backref=user >> is how many user in the Note Table [list]
                            backref='user', lazy='dynamic')
    # add all the note_id created by the user./.....


class sharedIds(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    note_id = db.Column(db.Integer, db.ForeignKey('note.id'))
    shred_by = db.Column(db.Integer, db.ForeignKey('user.id'))
