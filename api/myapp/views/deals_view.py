from flask import Blueprint,render_template, jsonify
import pandas as pd

from ..app import mysql


deals = Blueprint("deals",__name__)

@deals.route("/api/v1/dealsByYear_linePlot/")
def get_inv_analysis():
	df = pd.read_sql("SELECT * FROM investments", con=mysql.db)

