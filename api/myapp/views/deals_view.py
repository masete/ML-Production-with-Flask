from flask import Blueprint, jsonify, current_app
import pandas as pd

deals = Blueprint("deals", __name__)

@deals.route("/api/v1/dealsByYear_linePlot/")
def get_inv_analysis():
    mysql = current_app.config['MYSQL']
    db = mysql.db

    c = db.cursor()
    c.execute('''SELECT YEAR(`when`) AS year, COUNT(*) AS deal_count
                 FROM investments
                 GROUP BY year''')
    results = c.fetchall()

    # close cursor
    c.close()

    columns = [desc[0] for desc in c.description]  # Get column names from description

    df = pd.DataFrame(results, columns=columns)

    data = df.to_dict(orient='records')

    return jsonify(data)

# from flask import Blueprint, jsonify, current_app
# from .db import get_db_connection
# import pandas as pd
# import random
# import asyncio
# from ..app import mysql
# # from myapp.app import app



# deals = Blueprint("deals",__name__)


# async def get_inv_analysis():
#     db = await get_db_connection()
    
#     # Create a cursor object
#     cursor = await db.cursor()
    
#     try:
#         # Execute a query
#         await cursor.execute('''SELECT YEAR(`when`) AS year, COUNT(*) AS deal_count
#         FROM investments
#         GROUP BY year
        
#         ''')
        
#         # Fetch all rows
#         rows = await cursor.fetchall()
#         columns = [desc[0] for desc in cursor.description] # Get column names from description
#         df = pd.DataFrame(rows, columns=columns)
#         data = df.to_dict(orient='records')
#         return jsonify(data)
#         # Process the rows as needed
#         # for row in rows:
#             # Access row data using indexing or column names
#             # column1_value = row[0]
#             # column2_value = row["column_name"]
#             # Process the values
            
#     finally:
#         # Close the cursor
#         await cursor.close()


# 	# c = mysql.db.get_db()
# 	# c.execute('''SELECT YEAR(`when`) AS year, COUNT(*) AS deal_count
#     #     FROM investments
#     #     GROUP BY year''')
# 	# results = c.fetchall()

# 	# close cursor
# 	# c.close()

# 	# columns = [desc[0] for desc in c.description]  # Get column names from description

# 	# df = pd.DataFrame(results, columns=columns)

# 	# data = df.to_dict(orient='records')

# 	# return jsonify(data)

# @deals.route("/api/v1/dealsByYear_linePlot/")
# def deals_by_year_line_plot():
#     return asyncio.run(get_inv_analysis())

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

# @deals.route("/api/v1/quarteryValueOfInvestment/")
# def get_valueOfDealsByQuarter():
	
# 	query = '''
# 		SELECT
#     		CONCAT(YEAR(`when`), '-Q', QUARTER(`when`)) AS quarter,
#     		SUM(amount) DIV 1000000 AS quarterly_value
# 		FROM
#     		investments
# 		WHERE
#     		`when` BETWEEN '2019-01-01' AND '2023-12-31'
# 		GROUP BY
#     		quarter
	
# 	'''
	
# 	df = pd.read_sql_query(query, con=app.db)

# 	df['year'] = df['quarter'].str.extract('^(\d{4})')
# 	df['quarter'] = df['quarter'].str.extract('^(\d{4}-Q\d)')

# 	df = df.groupby(['year', 'quarter']).sum().reset_index()


# 	data = df.to_dict(orient='records')

# 	colors = {}

# 	for row in data:
# 		quarter = row["quarter"]
# 		if quarter not in colors:
# 			# generate a random color for each unique quarter
# 			colors[quarter] = '#' + ''.join(random.choices('0123456789ABCDEF', k=6))
# 		row["color"] = colors[quarter]

# 	return jsonify(data)

# @deals.route("/api/v1/dealsList/")
# def get_all_dealsList():
# 	c = app.db.cursor()
# 	c.execute('''SELECT * FROM investments''')
# 	results = c.fetchall()

# 	# close cursor
# 	c.close()

# 	columns = [desc[0] for desc in c.description]  # Get column names from description

# 	df = pd.DataFrame(results, columns=columns)

# 	data = df.to_dict(orient='records')

# 	return jsonify(data)
