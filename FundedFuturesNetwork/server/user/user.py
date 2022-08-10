from flask import Blueprint
from flask import current_app as app
from flask import jsonify
from flask import request
from flask import make_response
from pprint import pprint
from server.rithmic import crud

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/signup", methods=["POST"])
def signup():
	data = request.get_json(force=True)
	pprint(data)

	sql = """
	INSERT INTO FundedFuturesNetwork.Users (address, city, country, email, first, last, password, phone, postal, state, username)
	VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
	"""
	with app.db() as db:
		commit = db.commit(sql, data)
		sql = "INSERT INTO FundedFuturesNetwork.Subscriptions (username, tier) VALUES (%s, 0)"
		params = { 'username': data['username'] }

		if commit == 1:
			commit = db.commit(sql, params)
			crud.add_user(data)
			return jsonify({'message': "Signup successful", 'status': 200})

	return jsonify({'message': commit, 'status': 400})


@user_bp.route("/login", methods=["POST"])
def login():
	data = request.get_json(force=True)
	print(data)

	sql = "SELECT * FROM FundedFuturesNetwork.Users WHERE username=%s and password=%s"

	with app.db() as db:
		user = db.query(sql, data)

		if len(user) > 0:
			return jsonify({'message': "login", 'status': 200})

	return jsonify({'message': "Wrong username or password", 'status': 400})


@user_bp.route("/user", methods=["POST"])
def user():
	data = request.get_json(force=True)
	print(data)

	sql = """
	SELECT
		U.username,
		U.`first`,
		U.`last`,
		U.address,
		U.phone,
		U.email,
		S.tier,
		T.equity,
		T.friendly,
		U.systemDate AS 'accountCreated',
		S.systemDate AS 'dateSubscribed'
	FROM FundedFuturesNetwork.Users U
	LEFT JOIN FundedFuturesNetwork.Subscriptions S ON S.username=U.username
	LEFT JOIN FundedFuturesNetwork.Tiers T ON S.tier=T.id
	WHERE U.username=%s
	ORDER BY S.systemDate DESC
	LIMIT 1
	"""

	with app.db() as db:
		user = db.query(sql, data)

		if len(user) == 1:
			return jsonify({'message': user[0], 'status': 200})

	return jsonify({'message': "could not get user info", 'status': 400})


@user_bp.route("/user/memberships", methods=["POST"])
def user_memberships():
	data = request.get_json(force=True)
	sql = """
	SELECT *
	FROM Subscriptions S
	JOIN Tiers T ON T.id=S.tier
	WHERE S.username=%s
	ORDER BY S.systemDate DESC
	"""

	with app.db() as db:
		memberships = db.query(sql, data)
		if len(memberships) > 0:
			return jsonify({'message': memberships, 'status': 200})

	return jsonify({'message': "No memberships found", 'status': 400})


@user_bp.route("/user/purchase-membership", methods=["POST"])
def user_pucrchase_tier():
	data = request.get_json(force=True)
	sql = "INSERT INTO FundedFuturesNetwork.Subscriptions (username, tier) VALUES (%s, %s)"

	with app.db() as db:
		tier = db.commit(sql, data)
		if tier == 1:
			return jsonify({'message': "Purchased tier", 'status': 200})

	return jsonify({'message': "Could not purchase tier", 'status': 400})
