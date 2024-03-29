from flask import Blueprint, jsonify, current_app
from flask_cors import cross_origin
import pandas as pd

claim_profiles = Blueprint("claim_profiles", __name__)
mysql = None

@claim_profiles.before_request
def setup_mysql():
    global mysql
    mysql = current_app.config['MYSQL']


@claim_profiles.route("/api/v1/claim_profiles/")
@cross_origin()
def get_funds():
    try:
    
        with current_app.app_context():
            db = mysql.db

        c = db.cursor()
        c.execute('''SELECT * FROM claim_profiles''')
        results = c.fetchall()


        columns = [desc[0] for desc in c.description]  # Get column names from description

        df = pd.DataFrame(results, columns=columns)

        data = df.to_dict(orient='records')

        return jsonify(data)
    
    except Exception as e:
        print(f"Error: {e}")  # Debug statement
        return jsonify({'error': 'An error occurred'}), 500