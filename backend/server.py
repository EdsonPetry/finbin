from flask import Flask, jsonify, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
db = SQLAlchemy(app)
CORS(app)

@app.route('/', methods=['GET'])
def get_data():
    # data = {'message': 'Hello from Flask!'}
    # return jsonify(data)

    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")
if __name__ == "__main__":
    app.run(debug=True)