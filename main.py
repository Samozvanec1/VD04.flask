from flask import Flask

app = Flask(__name__)


@app.route('/') # служит для обозначения главной странички
def hello_world():
    return 'Hello World!'
@app.route('/new') # служит для обозначения главной странички
@app.route('/newpage/')
@app.route('/coolnewpage')
def hello_new():
    return 'New!'

if __name__ == '__main__':
    app.run()