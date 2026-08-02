from flask import Flask, request, render_template_string
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

# VULNERABILITY 1: Command Injection (Bad)
@app.route('/ping')
def ping():
    host = request.args.get('host', 'google.com')
    # This is terrible. Never do this.
    result = subprocess.check_output(f"ping -c 1 {host}", shell=True)
    return result

# VULNERABILITY 2: Server-Side Template Injection (SSTI)
@app.route('/greet')
def greet():
    name = request.args.get('name', 'Guest')
    template = f"<h1>Hello, {name}!</h1>"
    return render_template_string(template)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
