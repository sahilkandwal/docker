# app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! This is my Dockerized Python application.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
