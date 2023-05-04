# from flask import Blueprint,render_template, jsonify
# import pandas as pd

# from ..app import mysql


# deals = Blueprint("deals",__name__)


# @deals.route("/api/v1/deals/")
# def get_all_deals():

	
# 	cursor = mysql.db.cursor()
# 	cursor.execute('SELECT * FROM investments')
# 	results = cursor.fetchall()



# 	return jsonify({"all deals": results})


# @deals.route("/api/v1/invanalysis/")
# def get_inv_analysis():
# 	df = pd.read_sql("SELECT * FROM investments", con=mysql.db)