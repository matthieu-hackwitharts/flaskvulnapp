from flask import Flask
import os

app = Flask(__name__)

@app.route('/secret')
def hello():
    variables=""
    for name, value in os.environ.items():
        variables+= name + ":" + value
    return variables
    
@app.route('/')
def hello():
    return "Hello, Azure!"

if __name__ == '__main__':
    app.run()
