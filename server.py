from flask import Flask, request
import datetime

app = Flask(__name__)

attempts = {}
blocked_ips = set()
global_attempts = 0

# Load blocked IPs
try:
    with open("blocked.txt", "r") as f:
        for line in f:
            blocked_ips.add(line.strip())
except FileNotFoundError:
    pass

@app.route("/")
def home():
    return "Target server is running"

@app.route("/login")
def login():
    global global_attempts

    ip = request.remote_addr
    time = datetime.datetime.now()

    global_attempts += 1

    if global_attempts > 20:
        print("SIEM ALERT: Distributed attack suspected!")

    if ip in blocked_ips:
        with open("access.log", "a") as f:
            f.write(f"{time} - BLOCKED attempt from {ip}\n")
        return "Access denied", 403

    attempts[ip] = attempts.get(ip, 0) + 1

    with open("access.log", "a") as f:
        f.write(f"{time} - Login attempt from {ip}\n")

    if attempts[ip] > 5:
        print(f"⚠️ ALERT: Blocking IP {ip}")
        blocked_ips.add(ip)

        with open("blocked.txt", "a") as f:
            f.write(ip + "\n")

    return "Login page"

app.run(host="127.0.0.1", port=5000)
