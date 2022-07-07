from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager


db = SQLAlchemy()
db_name = 'fire1.db'


def Create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'robret-kohler'

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
        db_name  # db_name is a variable
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note, sharedIds
    Create_db(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.log'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app


def Create_db(app):
    if not os.path.exists('web'+db_name):
        db.create_all(app=app)
        print('Database created')
