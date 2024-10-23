from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    for name, value in os.environ.items():
        print("{0}: {1}".format(name, value))
    return "Hello, Azure!"

if __name__ == '__main__':
    app.run()
