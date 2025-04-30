import subprocess
from flask import Flask, request, abort, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h2>🚀 DevSecOps new command ru   </h2>
    <p>Welcome! Available endpoints:</p>
    <ul>
        <li><code>/run?cmd=ls</code> — Run a safe command (only 'ls' or 'whoami')</li>
        <li><code>/health</code> — Health check</li>
    </ul>
    """

@app.route('/health')
def health():
    return jsonify(status="ok", message="Flask app is running", version="1.0")

@app.route('/run')
def run_command():
    cmd = request.args.get('cmd')
    allowed_commands = ['ls', 'whoami']

    if cmd not in allowed_commands:
        abort(400, "Invalid command")

    result = subprocess.run([cmd], capture_output=True, text=True)
    return result.stdout

if __name__ == '__main__':
    print("✅ Flask app is starting on http://localhost:5000")
    app.run(host='0.0.0.0', port=5000)
