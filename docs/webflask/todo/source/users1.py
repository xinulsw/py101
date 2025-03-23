import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.exceptions import abort
from werkzeug.security import check_password_hash, generate_password_hash

from db import get_db

bp = Blueprint('users', __name__, template_folder='templates', url_prefix='/users')

@bp.route('/loguj', methods=['GET', 'POST'])
def loguj():
    if request.method == 'POST':
        login = request.form['login'].strip()
        haslo = request.form['haslo'].strip()

        db = get_db()
        error = None

        user = db.execute('SELECT * FROM user WHERE login = ?', [login]).fetchone()

        if user is None:
            error = 'Błędny login.'
        elif not check_password_hash(user['haslo'], haslo):
            error = 'Błędne hasło.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            flash(f'Zalogowano użytkownika {user['login']}!')
            return redirect(url_for('index'))
        flash(error)
    return render_template('users/loguj.html')
