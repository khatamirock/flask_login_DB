from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from pymongo import mongo_client

# Database setup

# conn_str = '''mongodb+srv://ronin:roninrocK1@cluster0.mp1aw.mongodb.net/login?retryWrites=true&w=majority'''
client = pymongo.MongoClient(os.getenv(“MONGODB_URI”, “mongodb://127.0.0.1:27017/database”))
login = client['login']


def Create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'robret-kohler'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
