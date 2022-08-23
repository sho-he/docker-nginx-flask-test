from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/api/hello', methods=["GET"])
def get_hello():
    return 'Backend'

@app.route('/api/get', methods=["GET"])
def get_flask():
    return "Flask"
