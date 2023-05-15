from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from pymongo import mongo_client
import os
# Database setup


mpass = os.environ['Mpass']
# conn_str = '''mongodb+srv://ronin:roninrocK1@cluster0.mp1aw.mongodb.net/login?retryWrites=true&w=majority'''

conn_str = '''mongodb+srv://{}@cluster0.mp1aw.mongodb.net/login?retryWrites=true&w=majority'''.format(mpass)
client = mongo_client.MongoClient(conn_str)
login = client['login']


def Create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'robret-kohler'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
