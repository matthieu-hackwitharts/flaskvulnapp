from flask import Flask
import subprocess

app = Flask(__name__)

def run_command(command):
    return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()

@app.route('/exec/<command>')
def command_server(command):
    return run_command(command)

@app.route('/')
def hello():
    return "Hello, Azure!"

if __name__ == '__main__':
    app.run()
