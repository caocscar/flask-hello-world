from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Hello Render benton!'

@application.route('/bye')
def bye():
    return '<h1>It was nice knowing you</h1>'