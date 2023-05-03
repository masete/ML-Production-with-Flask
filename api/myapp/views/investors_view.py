from flask import Blueprint,render_template, jsonify

from ..app import mysql


investor = Blueprint("investor",__name__)


@investor.route("/api/v1/investor/<int:id>")
def get_one_investor(id):

	
	c = mysql.db.cursor()
	c.execute('SELECT * FROM investors_v3')
	results = c.fetchone()
	return jsonify({"single investor": results})

