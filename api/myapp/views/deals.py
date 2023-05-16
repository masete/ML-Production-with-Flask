from flask import Blueprint, jsonify, current_app
import pandas as pd
import random

deals = Blueprint("deals", __name__)
mysql = None

@deals.before_app_first_request
def setup_mysql():
    global mysql
    mysql = current_app.config['MYSQL']

@deals.route("/api/v1/dealsByYear_linePlot/")
def get_inv_analysis():
    
    with current_app.app_context():
        db = mysql.db

    c = db.cursor()
    c.execute('''SELECT YEAR(`when`) AS year, COUNT(*) AS deal_count
                 FROM investments
                 GROUP BY year''')
    results = c.fetchall()

    # close cursor
    # c.close()

    columns = [desc[0] for desc in c.description]  # Get column names from description

    df = pd.DataFrame(results, columns=columns)

    data = df.to_dict(orient='records')

    return jsonify(data)

@deals.route("/api/v1/quarteryValueOfInvestment/")
def get_valueOfDealsByQuarter():
        
    with current_app.app_context():
        db = mysql.db

    c = db.cursor()
	
    query = '''
		SELECT
    		CONCAT(YEAR(`when`), '-Q', QUARTER(`when`)) AS quarter,
    		SUM(amount) DIV 1000000 AS quarterly_value
		FROM
    		investments
		WHERE
    		`when` BETWEEN '2019-01-01' AND '2023-12-31'
		GROUP BY
    		quarter
	
	'''
	
    df = pd.read_sql_query(query, con=c)

    df['year'] = df['quarter'].str.extract('^(\d{4})')
    df['quarter'] = df['quarter'].str.extract('^(\d{4}-Q\d)')

    df = df.groupby(['year', 'quarter']).sum().reset_index()


    data = df.to_dict(orient='records')

    colors = {}

    for row in data:
        quarter = row["quarter"]
        if quarter not in colors:
			# generate a random color for each unique quarter
            colors[quarter] = '#' + ''.join(random.choices('0123456789ABCDEF', k=6))
        row["color"] = colors[quarter]

    return jsonify(data)

@deals.route("/api/v1/dealsList/")
def get_all_dealsList():

    with current_app.app_context():
        db = mysql.db

    c = db.cursor()
    c.execute('''SELECT * FROM investments''')
    results = c.fetchall()

	# close cursor
	# c.close()

    columns = [desc[0] for desc in c.description]  # Get column names from description

    df = pd.DataFrame(results, columns=columns)

    data = df.to_dict(orient='records')

    return jsonify(data)
