from flask import Flask


def create_app():
    app = Flask(__name__)  # initializing flask
    app.config['SECRET-KEY'] = 'askjdfkhlasdf djsafslkdfhlaj'

    return app
