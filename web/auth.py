import email
from flask import Blueprint
from flask import render_template, request, redirect, url_for, flash, jsonify, session
from .models import User, Note
from . import db
from flask_login import login_user, logout_user, current_user, login_required


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        print('>>>>>>>>>>>>>>>>>', user)
        if user and user.password == password:
        # logTrue, usery = mongolog(username, password)
            flash('Welcome !!! {}'.format(username), category='success')
            login_user(user, remember=True)
            session['username'] = username
            session['userid'] = user.id
            return render_template('home.html', user=username+'! ')
            # return redirect(url_for('views.index', user=username))

        else:
            flash('NOTHIN in The DATABASE!!', category='error')

    return render_template('login.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    session.pop('username', None)
    session.pop('userid', None)

    return redirect(url_for('auth.log'))


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists', category='error')
            return redirect(url_for('auth.signup'))
        elif username == '' or password == '' or email == '':
            flash('Please fill all the fields', category='error')
        else:
            user = User(username=username, password=password, email=email)
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=True)
            flash('User created successfully', category='success')
            return redirect(url_for('auth.log'))

    return render_template('signup.html')
