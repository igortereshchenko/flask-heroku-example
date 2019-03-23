from flask import Flask, render_template

# create Flask instance
app = Flask(__name__)

# default route
@app.route('/')
def index():
    return render_template('index.html', names=['Bob','Boba','Boban'])

# route with string parameter, example: .../hello/Bob
@app.route('/hello/<name>')
def hello(name):
    return "Hello, {0}".format(name)
