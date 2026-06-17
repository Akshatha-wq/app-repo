##Triggering a fresh Build Tag
from flask import Flask, jsonify  # type: ignore[import]
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "success",
        "message": "Welcome to our GitOps Deployable App Container Engine!, this is a test app for GitOps deployment",
        "environment": os.getenv("ENVIRONMENT", "production")
        "version": "2.0.0"
    }), 200

@app.route('/healthz')
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)