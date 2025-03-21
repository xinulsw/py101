from flask import (
    Blueprint, flash, render_template, request, redirect, url_for
)
from db import get_db

bp = Blueprint('todo', __name__, template_folder='templates', url_prefix='/todo')

@bp.route('/')
def index():
    db = get_db()
    kursor = db.execute('SELECT * FROM zadania ORDER BY data_pub DESC;')
    zadania = kursor.fetchall()
    return render_template('todo/index.html', zadania=zadania)
