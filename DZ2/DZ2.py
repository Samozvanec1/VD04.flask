from flask import Flask
import flask
app = Flask(__name__)

@app.route('/')
def vosstan():
    return flask.render_template('index.html')

@app.route('/blog/')
def blog():
    return flask.render_template('blog.html')

@app.route('/contacts/')
def contacts():
    return flask.render_template('contacts.html')

if __name__ == '__main__':
    app.run()

