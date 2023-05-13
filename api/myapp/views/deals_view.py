from flask import Blueprint,render_template, jsonify
import pandas as pd


from ..app import mysql


deals = Blueprint("deals",__name__)


# @deals.route("/api/v1/dealsByYear_linePlot/")
# def get_inv_analysis():


# 	c = mysql.db.cursor()
# 	c.execute('''SELECT YEAR(`when`) AS year, COUNT(*) AS deal_count
#         FROM investments
#         GROUP BY year''')
# 	results = c.fetchall()

# 	columns = [desc[0] for desc in c.description]  # Get column names from description

# 	df = pd.DataFrame(results, columns=columns)

# 	data = df.to_dict(orient='records')

# 	return jsonify(data)

# @deals.route("/api/v1/valueOfDealsByCountry_barPlot/")
# def get_valueOfDeals():

# 	c = mysql.db.cursor()

# 	c.execute('''SELECT
#   			SUBSTRING_INDEX(countries_of_operation, ',', 1) as country,
#   			SUM(investments.amount) as total_amount
# 		FROM
#   			investments
#   			INNER JOIN companies_v3 ON investments.company = companies_v3.name
# 		GROUP BY
#   			country
# 			''')
# 	results = c.fetchall()

# 	if results:
# 		columns = [desc[0] for desc in c.description]  # Get column names from description
# 		data = [dict(zip(columns, row)) for row in results]  # Convert rows to dictionaries
# 		df = pd.DataFrame(results, columns=columns)

# 		data = df.to_dict(orient='records')

# 		return data
# 	else:
# 		data = []

	# columns = [desc[0] for desc in c.description]  # Get column names from description

	# df = pd.DataFrame(results, columns=columns)

	# data = df.to_dict(orient='records')

	# return data


# 	query = '''

		# SELECT
  		# 	SUBSTRING_INDEX(countries_of_operation, ',', 1) as country,
  		# 	SUM(investments.amount) as total_amount
		# FROM
  		# 	investments
  		# 	INNER JOIN companies_v3 ON investments.company = companies_v3.name
		# GROUP BY
  		# 	country;

# 	'''

# 	df = pd.read_sql_query(query, con=mysql.db)
# 	mysql.db.close()


# 	data = df.to_dict(orient='records')

# 	return data

@deals.route("/api/v1/quarteryValueOfInvestment/")
def get_valueOfDealsByQuarter():
	query = '''

		SELECT
    		CONCAT(YEAR(`when`), '-Q', QUARTER(`when`)) AS quarter,
    		SUM(amount) AS quarterly_value
		FROM
    		investments
		GROUP BY
    		quarter

	'''
	
	df = pd.read_sql_query(query, con=mysql.db)

	df['year'] = df['quarter'].str.extract('^(\d{4})')
	df['quarter'] = df['quarter'].str.extract('^(\d{4}-Q\d)')

	df = df.groupby(['year', 'quarter']).sum().reset_index()

	data = df.to_dict(orient='records')

# 	# colors = ["#FFC107", "#2196F3", "#4CAF50", "#FF5722"]
# 	# color_index = 0
# 	# for point in data:
# 	# 	point["color"] = colors[color_index]
# 	# 	color_index = (color_index + 1) % len(colors)

# 	# yrVposts = Unique_deals_df.year.value_counts()

	return jsonify(data)

# @deals.route("/api/v1/dealsList/")
# def get_all_dealsList():
# 	c = mysql.db.cursor()
# 	c.execute('''SELECT * FROM investments''')
# 	results = c.fetchall()

# 	columns = [desc[0] for desc in c.description]  # Get column names from description

# 	df = pd.DataFrame(results, columns=columns)

# 	data = df.to_dict(orient='records')

# 	return jsonify(data)
