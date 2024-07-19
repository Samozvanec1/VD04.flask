from flask import Flask
import flask

app = Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')
@app.route('/second/')
def second():
    return flask.render_template('second.html')
#     html = """
#     <h1>Hello, World!</h1>
#     <p>This is a paragraph.</p>
#     <p>This is another paragraph.</p>
#     <p>This is yet another paragraph.</p>
#     <p>This is yet another paragraph too.</p>
#     """
#     return html

if __name__ == '__main__':
    app.run()