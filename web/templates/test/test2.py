from mongoengine import *
import mongoengine as db
conn_str = '''mongodb+srv://ronin:roninrocK1@cluster0.mp1aw.mongodb.net/login?retryWrites=true&w=majority'''

connect(host=conn_str)


class user(db.Document):
    id = IntField(primary_key=True, required=True)
    username = StringField(max_length=50, required=True)
    password = StringField(max_length=50, required=True)
    email = StringField(max_length=50, required=True)

    def __repr__(self):
        return '<User %r>' % self.username


usr1 = user(id=36, username='manner', password='345',
            email='sdfsdf@hoga2.com')

usr1.save()

xx = user.objects.get(username='manner')
print(xx.password, xx.id)
