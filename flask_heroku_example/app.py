import os
from flask import Flask, render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'XYZ')




@app.route('/')
def index():

    return render_template('index.html', names=['Bob','Boba','Boban'])
