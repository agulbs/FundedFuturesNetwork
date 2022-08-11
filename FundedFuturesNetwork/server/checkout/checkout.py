from flask import Blueprint
from flask import current_app as app
from flask import jsonify
from flask import request
from flask import make_response
from pprint import pprint
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
		amount=data['purchase']['price'] * 100,
		currency="usd",
		description="test tier 1"
	)


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

	pprint(charge)
	return jsonify({'message': charge, 'status': 200})
