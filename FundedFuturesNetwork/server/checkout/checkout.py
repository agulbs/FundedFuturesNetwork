from flask import Blueprint
from flask import current_app as app
from flask import jsonify
from flask import request
from flask import make_response
from pprint import pprint
from server.rithmic import crud
import stripe

checkout_bp = Blueprint("checkout_bp", __name__)

stripe.api_key = "sk_test_51LVNKPKSvK2NDY9DYpI8IbVFdKbG9YvYCmwDQTNPorS4ZHtzybSH0DmECAe4nMwF6ODoG3HzVP8agoX8z6wQb6hQ00gzjtAV1W"


@checkout_bp.route("/checkout", methods=["POST"])
def checkout():
	data = request.get_json(force=True)
	pprint(data)

	customer = stripe.Customer.create(email=data['user']['email'], source=data['token']['id'])
	charge = stripe.Charge.create(
		customer=customer['id'],
		amount=int(data['purchase']['price'] * 100),
		currency="usd",
		description="test tier 1"
	)

	data['user']['reset'] = True
	if data['user']['tier'] == 0:
		data['user']['reset'] = False
	data['user']['cash'] = data['user']['equity']
	crud.add_account(data['user'])


	with app.db() as db:
		sql = "INSERT INTO FundedFuturesNetwork.Transactions (username, tier, price, package, receipt) VALUES (%s, %s, %s, %s, %s)"
		params = {
			'username': data['user']['username'],
			'tier': data['purchase']['id'],
			'price': data['purchase']['price'],
			'package': data['purchase']['status'],
			'receipt': charge['receipt_url']
		}

		db.commit(sql, params)

		if 'affiliateCode' in data['purchase']:
			sql = "INSERT INTO FundedFuturesNetwork.AffiliateUsed (username, code) VALUES (%s, %s)"
			params = { 'username': data['user']['username'], 'code':  data['purchase']['affiliateCode'] }
			db.commit(sql, params)

	return jsonify({'message': charge, 'status': 200})


@checkout_bp.route("/checkout/apply-discount", methods=["POST"])
def apply_discount():
	data = request.get_json(force=True)
	pprint(data)

	with app.db() as db:
		sql = "SELECT * FROM FundedFuturesNetwork.Affiliates A WHERE A.code=%s"
		discount = db.query(sql, {'affiliateCode': data['affiliateCode']})

		if len(discount) == 0:
			return jsonify({'message': "Discount code does not exist", 'status': 400})


		sql = "SELECT * FROM FundedFuturesNetwork.AffiliateUsed U WHERE U.username=%s"
		used_code = db.query(sql, {'username': data['user']['username']})
		if len(used_code) > 0:
			return jsonify({'message': "You have already used an affiliate code.", 'status': 400})

		return jsonify({'message': discount, 'status': 200})

	return jsonify({'message': "charge", 'status': 400})
