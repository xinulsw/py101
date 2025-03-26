from flask import (
    Blueprint, flash, g, render_template, request, redirect, url_for
)
from db import get_db
from users import login_required

bp = Blueprint('todo', __name__, template_folder='templates', url_prefix='/todo')

@bp.route('/')
@login_required
def index():
    db = get_db()
    sql = 'SELECT * FROM zadanie WHERE user_id=? ORDER BY data_pub DESC'
    zadania = db.execute(sql, [g.user['id']]).fetchall()
    return render_template('todo/index.html', zadania=zadania)

