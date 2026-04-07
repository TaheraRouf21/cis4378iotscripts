from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

LOG_FILE = "honeypot.log"

def log_attempt(ip, username, password):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.datetime.now()} | IP: {ip} | Username: {username} | Password: {password} | Route: /login\n")

@app.route('/')
def home():
    return "IoT Device Login"

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    ip = request.remote_addr

    log_attempt(ip, username, password)

    return jsonify({"status": "failed"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)