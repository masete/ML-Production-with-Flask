from flask import Blueprint,render_template, jsonify
import pandas as pd
# from mysql.connector import cnx

from ..app import mysql


deals = Blueprint("deals",__name__)

#Add year column from 1_post_date
# def get_year(dt):
# 	return dt.year

@deals.route("/api/v1/dealsByYear_linePlot/")
def get_inv_analysis():

	# query = '''
    #     SELECT YEAR(`when`) AS year, COUNT(*) AS deal_count
    #     FROM investments
    #     GROUP BY year
    # '''
    
	# df = pd.read_sql_query(query, con=mysql.db)


	# data = df.to_dict(orient='records')


	# yrVposts = Unique_deals_df.year.value_counts()

	# return data

	# execute the simplified query
	query = "SELECT YEAR(`when`) AS year, COUNT(*) AS deal_count FROM investments GROUP BY year;"
	mysql.db.execute(query)

	# fetch all the rows and print them
	rows = mysql.db.fetchall()
	for row in rows:
		print(row)
		df = pd.read_sql_query(query, con=mysql.db)
		data = df.to_dict(orient='records')
		return data

	# close the cursor and database connection
	mysql.db.close()
	mysql.db.close()
	


# @deals.route("/api/v1/valueOfDealsByCountry_barPlot/")
# def get_valueOfDeals():


# 	query = '''

# 		SELECT
#   			SUBSTRING_INDEX(countries_of_operation, ',', 1) as country,
#   			SUM(investments.amount) as total_amount
# 		FROM
#   			investments
#   			INNER JOIN companies_v3 ON investments.company = companies_v3.name
# 		GROUP BY
#   			country;

# 	'''

# 	df = pd.read_sql_query(query, con=mysql.db)



# 	# json_str = df.to_json(orient='records')
# 	data = df.to_dict(orient='records')

# 	# yrVposts = Unique_deals_df.year.value_counts()

# 	return data

# @deals.route("/api/v1/quarteryValueOfInvestment/")
# def get_valueOfDealsByQuarter():
# 	query = '''

# 		SELECT
#     		CONCAT(YEAR(`when`), '-Q', QUARTER(`when`)) AS quarter,
#     		SUM(amount) AS quarterly_value
# 		FROM
#     		investments
# 		GROUP BY
#     		quarter

# 	'''
	
# 	df = pd.read_sql_query(query, con=mysql.db)



# 	# json_str = df.to_json(orient='records')
# 	data = df.to_dict(orient='records')

# 	# colors = ["#FFC107", "#2196F3", "#4CAF50", "#FF5722"]
# 	# color_index = 0
# 	# for point in data:
# 	# 	point["color"] = colors[color_index]
# 	# 	color_index = (color_index + 1) % len(colors)

# 	# yrVposts = Unique_deals_df.year.value_counts()

# 	return data

# @deals.route("/api/v1/dealsList/")
# def get_all_dealsList():
# 	query = '''

# 		SELECT
#     		CONCAT(YEAR(`when`), '-Q', QUARTER(`when`)) AS quarter,
#     		SUM(amount) AS quarterly_value
# 		FROM
#     		investments
# 		GROUP BY
#     		quarter

# 	'''

# 	df = pd.read_sql_query(query, con=mysql.db)



# 	# json_str = df.to_json(orient='records')
# 	data = df.to_dict(orient='records')

# 	# yrVposts = Unique_deals_df.year.value_counts()

# 	return data
