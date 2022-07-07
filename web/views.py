
from sqlalchemy import text
from requests import session
from flask_login import login_user,  current_user, login_required
from flask import render_template, request, redirect, url_for, flash, jsonify
from flask import Blueprint
from .models import User, Note, sharedIds
from . import db
from traceback import print_tb
from codecs import ignore_errors


views = Blueprint('views', __name__)


@views.route('/')
@login_required
def index():
    return render_template('home.html')


@views.route('/create_notes', methods=['GET', 'POST'])
@login_required
@login_required
def create_notes():
    if request.method == 'POST':
        content = request.form['content']
        user_id = current_user.id
        shared = request.form['shared']
        share = shared.split(',')
        share += str(current_user.id)
# get all the id from note

        t = text("SELECT id FROM note")
        res = db.engine.execute(t)
        xx = res.fetchall()

        last_note = 1
        if xx != []:
            last_note = xx[-1][0] + 1

        for i in share:
            share = sharedIds(user_id=i, note_id=last_note,
                              shred_by=current_user.id)
            db.session.add(share)
            db.session.commit()

        note = Note(content=content, user_id=user_id, shared=shared)
        db.session.add(note)
        db.session.commit()

        redirect(url_for('views.index'))
    return render_template('notes_frm.html')


@views.route('/notes')
@login_required
def viewNotes():
    notes = current_user.notes
    res = db.session.query(sharedIds.note_id, Note.content, sharedIds.shred_by)\
            .join(Note).filter(sharedIds.user_id == current_user.id).distinct()

    return render_template('booklist.html', notes=res)
