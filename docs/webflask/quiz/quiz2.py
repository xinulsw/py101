# -*- coding: utf-8 -*-
# quiz/quiz.py

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Cześć, tu Python!'


if __name__ == '__main__':
    app.run(debug=True)
