from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Render Renton!'

@app.route('/bye')
def bye():
    return '<h1>It was nice knowing you</h1>'