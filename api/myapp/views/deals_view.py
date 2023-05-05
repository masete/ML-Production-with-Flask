from flask import Blueprint,render_template, jsonify
import pandas as pd

from ..app import mysql


deals = Blueprint("deals",__name__)

#Add year column from 1_post_date
def get_year(dt):
	return dt.year

@deals.route("/api/v1/dealsByYear_linePlot/")
def get_inv_analysis():

	# query = '''
    #     SELECT YEAR(`when`) AS year, COUNT(*) AS deal_count
    #     FROM investments
    #     GROUP BY year
    # '''

	query = '''
        SELECT ROW_NUMBER() OVER (ORDER BY YEAR(`when`)) AS id, YEAR(`when`) AS year, COUNT(*) AS deal_count
		FROM investments
		GROUP BY year

    '''
	
    
	df = pd.read_sql_query(query, con=mysql.db)

	# json_str = df.to_json(orient='records')
	data = df.to_dict(orient='records')

	# yrVposts = Unique_deals_df.year.value_counts()

	return data

