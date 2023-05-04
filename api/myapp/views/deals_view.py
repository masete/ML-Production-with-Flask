from flask import Blueprint,render_template, jsonify
import pandas as pd

from ..app import mysql


deals = Blueprint("deals",__name__)

#Add year column from 1_post_date
def get_year(dt):
	return dt.year

@deals.route("/api/v1/dealsByYear_linePlot/")
def get_inv_analysis():
	df = pd.read_sql("SELECT * FROM investments", con=mysql.db)

	df['year'] = df['1_post_date'].map(get_year)
	Unique_deals_df = df.drop_duplicates()

	yrVposts = Unique_deals_df.year.value_counts()

	return yrVposts

