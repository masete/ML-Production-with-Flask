from flask import Blueprint,render_template, jsonify

from ..app import mysql


deals = Blueprint("deals",__name__)


@deals.route("/api/v1/deals/")
def get_all_deals():

	
	cursor = mysql.db.cursor()
	cursor.execute('SELECT * FROM investments')
	results = cursor.fetchall()
	return jsonify({"all deals": results})
