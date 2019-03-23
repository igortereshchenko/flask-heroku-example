from whitenoise import WhiteNoise

# import variable app (Flask instanse) from file app.py
from app import app

# create WhiteNoise application as decorator of Flask application
application = WhiteNoise(app)

# connect WhiteNoise application with static files
application.add_files('static/', prefix='static/')
