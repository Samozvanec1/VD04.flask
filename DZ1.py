from flask import Flask
import datetime
app = Flask(__name__)

@app.route('/')
def time():
    return str(datetime.datetime.now())

if __name__ == '__main__':
    app.run()

