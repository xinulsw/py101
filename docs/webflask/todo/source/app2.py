import os
from flask import Flask, current_app, render_template
from db import init_app, init_db

app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY='bardzosekretnawartosc',
    DATABASE=os.path.join(app.root_path, 'db.sqlite'),
    SITE_NAME='Moje zadania'
))

init_app(app)

@app.route('/')
def index():
    # return 'Cześć, tu Python i Flask!'
    return render_template('index.html')

with app.app_context():
    if not os.path.exists(current_app.config['DATABASE']):
        init_db()
    if __name__ == "__main__":
        app.run(debug=True)
