from flask_login import UserMixin, login_user, logout_user, current_user, login_required

db = int(1234)


class note(db.Document):
    content = db.StringField(required=True)
    user_id = db.IntField(required=True)

    shared_by = db.IntField(required=True)

    def __repr__(self):
        return '<Note %r>' % self.content


class user(db.Document, UserMixin):

    id = db.IntField(primary_key=True)
    username = db.StringField(required=True)
    password = db.StringField(required=True)
    email = db.StringField(required=True)

    def __repr__(self):
        return '<User %r>' % self.username


class shared_ids(db.Document):

    id = db.IntField(primary_key=True)
    user_id = db.ListField(db.ReferenceField('user'))
    note_id = db.IntField(required=True)
    shared_by = db.IntField(required=True)
