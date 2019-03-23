from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', names=['Bob','Boba','Boban'])


@app.route('/hello<name>')
def index(name):
    return "Hello, {0}".format(name)
