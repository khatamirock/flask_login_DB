from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from numpy import empty


def anyOf(lst):
    for x in lst:
        if x is empty:
            return True


app = Flask(__name__)

app.secret_key = 'super secret key'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/testi', methods=['GET', 'POST'])
def tester():
    if request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            data = request.get_json()
            data['response'] = 'success :)'
            return jsonify(data)
        elif request.headers['Content-Type'] == 'text/plain':
            data = request.data.decode('utf-8')
            return "Text Message: " + data
        else:
            return '415 Unsupported Media Type ;)'
    else:
        return 'get method broooo!!'


@app.route('/details', methods=['POST'])
def details():
    lname = request.form.get('l-name')
    fname = request.form.get('f-name')
    email = request.form.get('email')

    if lname is '' or fname is '' or email is '':
        flash('Please fill in all fields')
        return redirect(url_for('index'))

    return render_template('details.html', fname=fname, lname=lname, email=email)


app.run(debug=True)
