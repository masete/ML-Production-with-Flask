from flask import Blueprint, jsonify, current_app
from flask_cors import cross_origin
import time
import pandas as pd

exits_bp = Blueprint("exits_bp", __name__)
mysql = None


# def date2int(df):
#     if df.when:
#         t=df['when']
#         try:
#             t1=t.timetuple()
#             return int(time.mktime(t1))
#         except ValueError:
#             return None

@exits_bp.before_request
def setup_mysql():
    global mysql
    mysql = current_app.config['MYSQL']


@exits_bp.route("/api/v1/get_all_exits/")
@cross_origin()
def get_funds():
    try:
    
        with current_app.app_context():
            db = mysql.db

        c = db.cursor()
        c.execute('''SELECT * FROM exits''')
        results = c.fetchall()


        columns = [desc[0] for desc in c.description]  # Get column names from description

        df = pd.DataFrame(results, columns=columns)
        df=df.dropna()
        # df['date2int']=df.apply(date2int,axis=1)

        data = df.to_dict(orient='records')

        return jsonify(data)
    
    except Exception as e:
        print(f"Error: {e}")  # Debug statement
        return jsonify({'error': 'An error occurred'}), 500