from flask import Flask, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/bandwidth', methods=['GET'])
def get_bandwidth():
    result = subprocess.run(['vnstat', '--json', 'd'], capture_output=True, text=True)
    data = result.stdout
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
