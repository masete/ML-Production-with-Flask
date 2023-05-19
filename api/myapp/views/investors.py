from flask import Blueprint, jsonify, current_app
import pandas as pd

investors = Blueprint("investors", __name__)
mysql = None

@investors.before_app_first_request
def setup_mysql():
    global mysql
    mysql = current_app.config['MYSQL']

@investors.route("/api/v1/investorsByCountry/")
def get_invByCountry():
    
    with current_app.app_context():
        db = mysql.db

    c = db.cursor()
    c.execute('''SELECT 
                    CASE 
                        WHEN TRIM(SUBSTRING_INDEX(headquarters, ',', -1)) = '' OR headquarters IS NULL THEN 'Unknown'
                        WHEN TRIM(SUBSTRING_INDEX(headquarters, ',', -1)) = 'Lagos' THEN 'Nigeria'
                        WHEN TRIM(SUBSTRING_INDEX(headquarters, ',', -1)) = 'Johannesburg' THEN 'South Africa'
                        WHEN TRIM(SUBSTRING_INDEX(headquarters, ',', -1)) = 'California' THEN 'USA'
                        WHEN TRIM(SUBSTRING_INDEX(headquarters, ',', -1)) = 'Cape Town' THEN 'South Africa'
                        WHEN TRIM(SUBSTRING_INDEX(headquarters, ',', -1)) = 'Nairobi' THEN 'Kenya'
                        WHEN TRIM(SUBSTRING_INDEX(headquarters, ',', -1)) = 'Washington' THEN 'USA'
                        WHEN TRIM(SUBSTRING_INDEX(headquarters, ',', -1)) = 'San Francisco' THEN 'USA'
                        WHEN TRIM(SUBSTRING_INDEX(headquarters, ',', -1)) = 'New York' THEN 'USA'
                        WHEN TRIM(SUBSTRING_INDEX(headquarters, ',', -1)) = 'Cairo' THEN 'Egypt'
                        WHEN TRIM(SUBSTRING_INDEX(headquarters, ',', -1)) = 'Paris' THEN 'France'
                        WHEN TRIM(SUBSTRING_INDEX(headquarters, ',', -1)) = 'Dubai' THEN 'United Arab Emirates'
                        WHEN TRIM(SUBSTRING_INDEX(headquarters, ',', -1)) = 'London' THEN 'UK'
                        ELSE TRIM(SUBSTRING_INDEX(headquarters, ',', -1))
                    END AS country,
                    COUNT(*) AS investor_count
                    FROM investors_v3
                    GROUP BY country
                    ORDER BY investor_count DESC
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

@investors.route("/api/v1/investorsBySector/")
def get_invBySector():
    
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

