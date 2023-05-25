from flask import Blueprint, jsonify, current_app
from flask_cors import cross_origin
import pandas as pd

investors = Blueprint("investors", __name__)
mysql = None

@investors.before_request
def setup_mysql():
    global mysql
    mysql = current_app.config['MYSQL']

@investors.route("/api/v1/investorsByCountry/")
@cross_origin()
def get_invByCountry():

    try:
    
        with current_app.app_context():
            db = mysql.db

        c = db.cursor()
        c.execute('''SELECT
                        selected_headqtrs AS country,
                        COUNT(*) AS investor_count
                    FROM
                        investors_v3
                    GROUP BY
                        selected_headqtrs
                    ORDER BY
                        investor_count DESC
                    LIMIT 20;
                        ''')
        results = c.fetchall()

        columns = [desc[0] for desc in c.description]  # Get column names from description

        # df = pd.DataFrame(results, columns=columns)

        # c.close()

        columns = [desc[0] for desc in c.description]  # Get column names from description

        df = pd.DataFrame(results, columns=columns)

        data = df.to_dict(orient='records')

        return jsonify(data)
    
    except Exception as e:
        print(f"Error: {e}")  # Debug statement
        return jsonify({'error': 'An error occurred'}), 500

@investors.route("/api/v1/investorsBySector/")
def get_invBySector():

     try:
    
        with current_app.app_context():
            db = mysql.db

        c = db.cursor()
        c.execute('''

        SELECT
                        TRIM(SUBSTRING_INDEX(SUBSTRING_INDEX(sector_of_focus, ',', n.n), ',', -1)) AS sector_of_focus,
                        COUNT(*) AS investor_count
                    FROM investors_v3
                    JOIN (
                        SELECT 1 AS n UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 -- Add more numbers based on the maximum number of sectors in a row
                    ) n ON CHAR_LENGTH(sector_of_focus) - CHAR_LENGTH(REPLACE(sector_of_focus, ',', '')) >= n.n - 1
                    GROUP BY TRIM(SUBSTRING_INDEX(SUBSTRING_INDEX(sector_of_focus, ',', n.n), ',', -1));

                        ''')
        results = c.fetchall()

        columns = [desc[0] for desc in c.description]  # Get column names from description

        # df = pd.DataFrame(results, columns=columns)

        # c.close()

        columns = [desc[0] for desc in c.description]  # Get column names from description

        df = pd.DataFrame(results, columns=columns)

        data = df.to_dict(orient='records')

        return jsonify(data)
     
     except Exception as e:
        print(f"Error: {e}")  # Debug statement
        return jsonify({'error': 'An error occurred'}), 500

