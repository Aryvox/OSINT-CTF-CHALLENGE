from flask import Flask, request, jsonify
from config.settings import API_KEY, FLAG

app = Flask(__name__)

@app.route("/track", methods=["GET"])
def track_package():
    api_key = request.headers.get("Authorization")
    
    if api_key == f"Bearer {API_KEY}":
        return jsonify({"status": "delivered", "destination": "CTF HQ", "flag": FLAG})
    
    return jsonify({"error": "Invalid API key"}), 403

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
