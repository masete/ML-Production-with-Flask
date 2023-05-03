from flask import Blueprint,render_template, jsonify

from ..app import mysql


deals = Blueprint("deals",__name__)


@deals.route("/api/v1/deals/")
def get_all_deals():

	
	c = mysql.db.cursor()
	c.execute('SELECT * FROM investment')
	results = c.fetchall()
	return jsonify({"all deals": results})
