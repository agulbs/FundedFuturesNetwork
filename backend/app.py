from flask import Flask, jsonify, request, make_response, jsonify
from flask_cors import CORS, cross_origin
from db import DB
from pprint import pprint

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'castlefin-golf-tourn'
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

application = app

@app.route("/")
def home():
    return "201"

@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json(force=True)
    data['username'] = data['email']

    sql = "INSERT INTO FundedFuturesNetwork.Users (First, Last, Address, Phone, Email, Password, Username) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    db = DB()
    with db:
        commit = db.commit(sql, data)
        sql = "INSERT INTO FundedFuturesNetwork.Subscriptions (Username, Tier) VALUES (%s, 0)"
        params = { 'username': data['username'] }

        if commit == 1:
            commit = db.commit(sql, params)
            return jsonify({'message': "Signup successful", 'status': 200})

    return jsonify({'message': commit, 'status': 400})

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json(force=True)

    sql = "SELECT * FROM FundedFuturesNetwork.Users WHERE Username=%s and Password=%s"

    with DB() as db:
        user = db.query(sql, data)

        if len(user) > 0:
            return jsonify({'message': "login", 'status': 200})

    return jsonify({'message': "Wrong username or password", 'status': 400})

if __name__ == "__main__":
   app.run(debug=True)
