

import email
from flask import Blueprint
from flask import render_template, request, redirect, url_for, flash, jsonify, session
from . import login
# imports>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>####################


auth = Blueprint('auth', __name__)


def mongolog(user, pas):

    usr = login['user'].find_one({'username': user})
    print(usr['password'], usr['username'])
    if usr['username'] == user and usr['password'] == pas:
        return True, usr
    else:
        return False


@auth.route('/login', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # usery = User.query.filter_by(username=username).first()
        # print(usery)
        # if user and user.password == password:
        print(username, password)
        logTrue, use = mongolog(username, password)
        print(logTrue, use['username'])
        if logTrue:
            flash('Welcome !!! {}'.format(username), category='success')
            # ur = user()
            session['username'] = username
            session['userid'] = use['id']
            return render_template('home.html', user=username+'! ')
            # return redirect(url_for('views.index', user=username))

        else:
            flash('NOTHIN in The DATABASE!!', category='error')

    return render_template('login.html')


@auth.route('/logout')
def logout():

    session.pop('username', None)
    session.pop('userid', None)

    return redirect(url_for('auth.log'))


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        usr = login['user'].find_one({'username': username})

        id = login['user'].count_documents({})+1
        print(id)

        if usr:
            flash('Username already exists', category='error')
            return redirect(url_for('auth.signup'))
        elif username == '' or password == '' or email == '':
            flash('Please fill all the fields', category='error')
        else:
            login['user'].insert_one(
                {'id': id, 'username': username, 'password': password, 'email': email})

            flash('User created successfully', category='success')
            return redirect(url_for('auth.log'))

    return render_template('signup.html')
