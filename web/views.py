import re
from flask import Blueprint, render_template, request, redirect, url_for, session
from . import login
views = Blueprint('views', __name__)


@views.route('/')
def index():
    print(session)
    if session and 'username' in session:
        return render_template('home.html')
    else:
        # flash('Please LOGIN first', category='error')
        return redirect(url_for('auth.log'))


@views.route('/create_notes', methods=['GET', 'POST'])
def create_notes():
    if request.method == 'POST':
        content = request.form['content']
        user_id = session['userid']
        shared = request.form['shared']
        id = login['note'].count_documents({})+1
        share = set(shared.split(','))
        shrLst = [int(x) for x in share]+[int(session['userid'])]

        login['note'].insert_one(
            {'id': id, 'content': content, 'user_id': user_id})
        for i in shrLst:
            print(i)
            login['shared_ids'].insert_one({'note_id': id,
                                            'shared_by': user_id,
                                            'user_id': i})

        return redirect(url_for('views.index'))
    return render_template('notes_frm.html')


@views.route('/notes')
def viewNotes():
    userid = session['userid']

    res = login['shared_ids'].find({'user_id': int(userid)})
    note = login['note']
    # print(userid, list(res))
    notels = []
    # for x, i in enumerate(list(res)):

    for x in res:
        id = x['note_id']
        notels.append(note.find_one({'id': id}))
    # noteList = [x if x in]
    # return redirect(url_for('views.index'))
    return (render_template('booklist.html', ref=res, notes=notels, user=userid))


@views.route('/delete')
def delete():
    id = request.args.get('id')
    note = note.query.filter_by(id=id).first()
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            return redirect(url_for('views.viewNotes'))
    return redirect(url_for('views.viewNotes'))
