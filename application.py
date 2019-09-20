from flask import Flask
application = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Render benton!'

@app.route('/bye')
def bye():
    return '<h1>It was nice knowing you</h1>'