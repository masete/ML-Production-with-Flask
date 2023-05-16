from flask import Blueprint, jsonify, current_app
import pandas as pd

deals = Blueprint("deals", __name__)
mysql = current_app.config['MYSQL']

@deals.route("/api/v1/dealsByYear_linePlot/")
def get_inv_analysis():
    
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

@deals.route("/api/v1/dealsList/")
def get_all_dealsList():
    
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
