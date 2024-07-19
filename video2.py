from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/<password>/')
def hello_new(password):
    if password == '12345':
        return 'New!'
    else:
        return 'Hello World!'

if __name__ == '__main__':
    app.run()