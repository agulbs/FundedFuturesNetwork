from flask import Blueprint
from flask import current_app as app
from flask import jsonify
from flask import request
from flask import make_response


tiers_bp = Blueprint("tiers_bp", __name__)

@tiers_bp.route("/tiers", methods=["GET"])
def tiers():
	sql = "SELECT * FROM Tiers"
	with app.db() as db:
		tiers = db.query(sql, {})

		if len(tiers) > 0:
			return jsonify({'message': tiers, 'status': 200})

	return jsonify({'message': "could not get tier info", 'status': 400})
