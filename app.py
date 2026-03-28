from flask import Flask, request, jsonify, send_from_directory
import requests
import os

app = Flask(__name__, static_folder='static')

N8N_WEBHOOK_URL = os.environ.get('N8N_WEBHOOK_URL', 'https://alex-resorius.amvera.io/webhook/Chat')

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    try:
        response = requests.post(
            N8N_WEBHOOK_URL,
            json=data,
            headers={'Content-Type': 'application/json'},
            timeout=30
        )
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
