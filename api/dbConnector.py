from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL database settings
# app.config['MYSQL_HOST'] = 'digestafrica-do-user-4558844-0.b.db.ondigiio0talocean.com'
# app.config['MYSQL_USER'] = 'doaufddmin'
# app.config['MYSQL_PASSWORD'] = 'AVNS_Osw-cqylkgfdsH-pc7-_kHDkd'
# app.config['MYSQL_DB'] = 'defaupoytrwwxltdb'

# Initialize the MySQL extension
mysql = MySQL(app)

@app.route('/')
def index():
    # Execute a SQL query
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM acquisitons")
    results = cur.fetchall()
    cur.close()

    # Return the results as a response
    response = ''
    for row in results:
        response += str(row) + '<br>'
        print(response)
    return response



if __name__ == '__main__':
    app.run()
