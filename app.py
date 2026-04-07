from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "IoT Simulation Running"

@app.route("/device")
def device():
    user_input = request.args.get("host", "")

    # detect suspicious patterns
    suspicious_patterns = [";", "&&", "|", "$(", "`"]
    is_suspicious = any(pattern in user_input for pattern in suspicious_patterns)

    log_entry = {
        "time": str(datetime.datetime.now()),
        "input": user_input,
        "suspicious": is_suspicious,
        "ip": request.remote_addr
    }

    print(log_entry, flush=True)

    # to save the file
    with open("logs.txt", "a") as f:
        f.write(str(log_entry) + "\n")

    if is_suspicious:
        return jsonify({"status": "warning", "message": "Suspicious input detected"})
    else:
        return jsonify({"status": "ok", "message": "Normal input processed"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)