from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    # return 'Cześć, tu Python i Flask!'
    return render_template('index.html')

with app.app_context():
    if __name__ == "__main__":
        app.run(debug=True)
