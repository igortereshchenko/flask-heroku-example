# import variable app (Flask instanse) from file app.py
from app import app


if __name__ == '__main__':
    # setup debug mode and run Flask instanse
    app.debug = True
    app.run()
