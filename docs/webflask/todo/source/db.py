import sqlite3
from flask import g, current_app

def get_db():
    """Funkcja tworzy połączenie z bazą"""
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types = sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    """Funkcja zamyka połączenia z bazą"""
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_app(app):
    """Funkcja rejestruje funkcję close_db() w aplikacji"""
    app.teardown_appcontext(close_db)

def init_db():
    """Funkcja tworzy bazę i tabele"""
    db = get_db()
    with current_app.open_resource('todo.sql') as f:
        db.executescript(f.read().decode('utf8'))
