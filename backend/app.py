from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows cross-origin requests from frontend

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    return jsonify({
        'message': 'Data received successfully',
        'data': data
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)