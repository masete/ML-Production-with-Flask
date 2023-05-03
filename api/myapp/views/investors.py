from flask import Blueprint,render_template, jsonify

from ..app import mysql


investors = Blueprint("investors",__name__)


@investors.route("/api/v1/investor/<int:id>")
def get_one_investor(id):
	print("masete n")

	
	c = mysql.db.cursor()
	c.execute('SELECT * FROM acquisitions')
	results = c.fetchone()
	return jsonify({"single investor": results})
	

@investors.route("/api/v1/investor/")
def get_all_investor(id):
	print("masete n")

	
	c = mysql.db.cursor()
	c.execute('SELECT * FROM acquisitions')
	results = c.fetchall()
	return jsonify({"all investor": results})