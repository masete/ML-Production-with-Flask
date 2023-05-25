from flask import Blueprint, jsonify, current_app, g
from flask_cors import cross_origin
import pandas as pd


deals = Blueprint("deals", __name__)
mysql = None

@deals.before_request
def setup_mysql():
    global mysql
    mysql = current_app.config['MYSQL']

# @deals.route("/api/v1/update_inv/")
# @cross_origin()
# def update_inv_analysis1():
#     try:
    
#         with current_app.app_context():
#             db = mysql.db

#         c = db.cursor()

#             # Execute the SELECT query to fetch the results
#         c.execute("SELECT selected_headqtrs FROM investors_v3")

#             # Fetch all the rows
#         rows = c.fetchall()

#             # Create a new cursor for the UPDATE statement
#         update_cursor = db.cursor()

#             # Update the values in the selected_headqtrs column
#         update_cursor.execute("""
#             UPDATE investors_v3
#             SET selected_headqtrs =
#                 CASE
#                     WHEN selected_headqtrs = 'Lagos' THEN 'Nigeria'
#                     WHEN selected_headqtrs = 'Johannesburg' THEN 'South Africa'
#                     WHEN selected_headqtrs = 'California' THEN 'USA'
#                     WHEN selected_headqtrs = 'Cape Town' THEN 'South Africa'
#                     WHEN selected_headqtrs = 'Nairobi' THEN 'Kenya'
#                     WHEN selected_headqtrs = 'Washington' THEN 'USA'
#                     WHEN selected_headqtrs = 'San Francisco' THEN 'USA'
#                     WHEN selected_headqtrs = 'New York' THEN 'USA'
#                     WHEN selected_headqtrs = 'Cairo' THEN 'Egypt'
#                     WHEN selected_headqtrs = 'Paris' THEN 'France'
#                     WHEN selected_headqtrs = 'Dubai' THEN 'United Arab Emirates'
#                     WHEN selected_headqtrs = 'London' THEN 'UK'
#                     ELSE selected_headqtrs
#                 END
#         """)

#             # Commit the changes
#         db.commit()

#             # Close the cursors
#         c.close()
#         update_cursor.close()

#         return jsonify({'message': 'Update successful'})

#     except Exception as e:
#         print(f"Error: {e}")
#         return jsonify({'error': 'An error occurred'}), 500

# @deals.route("/api/v1/get_all_inv/")
# @cross_origin()
# def get_inv_analysis1():
#     try:
    
#         with current_app.app_context():
#             db = mysql.db

#         c = db.cursor()
#         c.execute('''SELECT * FROM investors_v3''')
#         results = c.fetchall()


#         columns = [desc[0] for desc in c.description]  # Get column names from description

#         df = pd.DataFrame(results, columns=columns)

#         data = df.to_dict(orient='records')

#         return jsonify(data)
    
#     except Exception as e:
#         print(f"Error: {e}")  # Debug statement
#         return jsonify({'error': 'An error occurred'}), 500

@deals.route("/api/v1/dealsByYear_linePlot/")
@cross_origin()
def get_inv_analysis():

    try:

    
        with current_app.app_context():
            db = mysql.db

        c = db.cursor()
        c.execute('''   SELECT
                        ROW_NUMBER() OVER (ORDER BY year) AS id,
                        COUNT(*) AS deal_count,
                            year
                        FROM
                            investments
                        GROUP BY
                            year;

                        ''')
        results = c.fetchall()


        columns = [desc[0] for desc in c.description]  # Get column names from description

        df = pd.DataFrame(results, columns=columns)

        data = df.to_dict(orient='records')

        return jsonify(data)
    
    except Exception as e:
        print(f"Error: {e}")  # Debug statement
        return jsonify({'error': 'An error occurred'}), 500


@deals.route("/api/v1/valueOfDealsByCountry_barPlot/")
@cross_origin()
def get_valueOfDeals():

    try:
        
        with current_app.app_context():
                db = mysql.db

        c = mysql.db.cursor()

        c.execute('''SELECT
                        SUBSTRING_INDEX(investments.selected_country, ',', 1) AS country,
                        SUM(investments.amount) AS total_amount
                    FROM
                        investments
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
    
    except Exception as e:
        print(f"Error: {e}")  # Debug statement
        return jsonify({'error': 'An error occurred'}), 500




@deals.route("/api/v1/quarteryValueOfInvestment/")
@cross_origin()
def get_valueOfDealsByQuarter():

    try:

        
        with current_app.app_context():
            db = mysql.db

        c = db.cursor()
        
        c.execute( '''
                                    SELECT
                                    CONCAT(year,'-',quarter) AS quarter,
                                        selected_country,
                                    SUM(amount) AS total_amount
                                    FROM
                                        investments
                                    GROUP BY
                                        year, quarter, selected_country
                                    ORDER BY
                                        year, quarter;
        ''')
    
        
        columns = [desc[0] for desc in c.description]
        print(columns)  # Debug statement
        df = pd.DataFrame(c.fetchall(), columns = columns)


        # df['year'] = df['quarter'].str.extract('^(\d{4})')
        # df['quarter'] = df['quarter'].str.extract('^(\d{4}-Q\d)')

        # df = df.groupby(['year', 'quarter']).sum().reset_index()


        data = df.to_dict(orient='records')

        return jsonify(data)
    
    except Exception as e:
        print(f"Error: {e}")  # Debug statement
        return jsonify({'error': 'An error occurred'}), 500

@deals.route("/api/v1/dealsList/<int:page>")
@cross_origin()
def get_all_dealsList(page):

     try:

        with current_app.app_context():
            db = mysql.db

        items_per_page = 6 # Number of items per page
        offset = (page - 1) * items_per_page

        c = db.cursor()
        c.execute("SELECT * FROM investments LIMIT %s OFFSET %s", (items_per_page, offset))

        results = c.fetchall()

        columns = [desc[0] for desc in c.description]  # Get column names from description

        df = pd.DataFrame(results, columns=columns)

        data = df.to_dict(orient='records')

        return jsonify(data)
     
     except Exception as e:
        print(f"Error: {e}")  # Debug statement
        return jsonify({'error': 'An error occurred'}), 500

@deals.route("/api/v1/dealsVsStage/")
@cross_origin()
def get_dealsVsStage():

    try:

        with current_app.app_context():
            db = mysql.db

        c = db.cursor()
        c.execute('''
                SELECT year AS Year, COUNT(*) AS DealCount, 
        CASE 
            WHEN funding_round = '' THEN 'undisclosed'
            ELSE funding_round
        END AS FundingRoundStage
FROM investments
GROUP BY Year, FundingRoundStage;


        ''')
        results = c.fetchall()

        columns = [desc[0] for desc in c.description]  # Get column names from description

        df = pd.DataFrame(results, columns=columns)

        data = df.to_dict(orient='records')

        return jsonify(data)
    
    except Exception as e:
        print(f"Error: {e}")  # Debug statement
        return jsonify({'error': 'An error occurred'}), 500
    
