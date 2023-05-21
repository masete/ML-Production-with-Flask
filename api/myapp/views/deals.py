from flask import Blueprint, jsonify, current_app
from flask_cors import cross_origin
import pandas as pd


deals = Blueprint("deals", __name__)
mysql = None

@deals.before_app_first_request
def setup_mysql():
    global mysql
    mysql = current_app.config['MYSQL']

@deals.route("/api/v1/dealsByYear_linePlot/")
@cross_origin()
def get_inv_analysis():
    
    with current_app.app_context():
        db = mysql.db

    c = db.cursor()
    c.execute('''SELECT
                    ROW_NUMBER() OVER (ORDER BY YEAR(`when`)) AS id,
                    COUNT(*) AS deal_count,
                    YEAR(`when`) AS year
                FROM
                    investments
                GROUP BY
                    year;
                    ''')
    results = c.fetchall()

    c.close()

    columns = [desc[0] for desc in c.description]  # Get column names from description

    df = pd.DataFrame(results, columns=columns)

    data = df.to_dict(orient='records')

    return jsonify(data)


@deals.route("/api/v1/valueOfDealsByCountry_barPlot/")
@cross_origin()
def get_valueOfDeals():

	c = mysql.db.cursor()

	c.execute('''SELECT
  			SUBSTRING_INDEX(countries_of_operation, ',', 2) as country,
  			SUM(investments.amount) as total_amount
		FROM
  			investments
  			INNER JOIN companies_v3 ON investments.company = companies_v3.name
		GROUP BY
  			country
        ORDER BY
            total_amount DESC
        LIMIT 10;
			''')
    
	results = c.fetchall()


	if results:
		columns = [desc[0] for desc in c.description]  # Get column names from description
		data = [dict(zip(columns, row)) for row in results]  # Convert rows to dictionaries
		df = pd.DataFrame(results, columns=columns)

		data = df.to_dict(orient='records')

		return data
	else:
		data = []

	columns = [desc[0] for desc in c.description]  # Get column names from description

	df = pd.DataFrame(results, columns=columns)

	data = df.to_dict(orient='records')
 

	return data




@deals.route("/api/v1/quarteryValueOfInvestment/")
@cross_origin()
def get_valueOfDealsByQuarter():
        
    with current_app.app_context():
        db = mysql.db

    c = db.cursor()
	
    c.execute( '''
                SELECT
            CONCAT(YEAR(`when`), '-Q', QUARTER(`when`)) AS quarter,
            SUM(amount) DIV 1000000 AS quarterly_value
        FROM
            investments
        WHERE
            `when` BETWEEN '2020-01-01' AND '2023-12-31'
        GROUP BY
            CONCAT(YEAR(`when`), '-Q', QUARTER(`when`))

	
	''')
   
    
    columns = [desc[0] for desc in c.description]
    df = pd.DataFrame(c.fetchall(), columns = columns)


    df['year'] = df['quarter'].str.extract('^(\d{4})')
    df['quarter'] = df['quarter'].str.extract('^(\d{4}-Q\d)')

    df = df.groupby(['year', 'quarter']).sum().reset_index()


    data = df.to_dict(orient='records')

    return jsonify(data)

@deals.route("/api/v1/dealsList/<int:page>")
@cross_origin()
def get_all_dealsList(page):

    with current_app.app_context():
        db = mysql.db

    items_per_page = 6 # Number of items per page
    offset = (page - 1) * items_per_page

    c = db.cursor()
    c.execute("SELECT * FROM investments LIMIT %s OFFSET %s", (items_per_page, offset))

    # c.execute("SELECT * FROM investments LIMIT %s OFFSET %s", (items_per_page, offset))
    results = c.fetchall()

    columns = [desc[0] for desc in c.description]  # Get column names from description

    df = pd.DataFrame(results, columns=columns)

    data = df.to_dict(orient='records')

    return jsonify(data)

@deals.route("/api/v1/dealsVsStage/")
@cross_origin()
def get_dealsVsStage():

    with current_app.app_context():
        db = mysql.db

    c = db.cursor()
    c.execute('''
            SELECT DATE_FORMAT(`when`, '%Y') AS Year, COUNT(*) AS DealCount, 
       CASE 
           WHEN funding_round = '' THEN 'undisclosed'
           ELSE funding_round
       END AS FundingRoundStage
        FROM investments
        WHERE `when` >= '2019-01-01'
        GROUP BY Year, FundingRoundStage

    ''')
    results = c.fetchall()

    columns = [desc[0] for desc in c.description]  # Get column names from description

    df = pd.DataFrame(results, columns=columns)

    data = df.to_dict(orient='records')

    return jsonify(data)
