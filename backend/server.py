from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

"""
    We need to GET recent account transactions from the user

    User should be able to create a new bucket

    
"""
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'message': 'Hello from Flask!'}
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)