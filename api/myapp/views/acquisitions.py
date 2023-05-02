from flask import Blueprint,render_template, jsonify

from ..app import mysql


# hello = Blueprint('hello',__name__)
acquisitions = Blueprint("acquisitions",__name__)


@acquisitions.route("/api/v1/acquisition/<int:id>")
def get_one_acquisition(id):
	print("masete n")

	
	c = mysql.db.cursor()
	c.execute('SELECT * FROM acquisitions')
	results = c.fetchone()
	return jsonify({"single acquisition": results})
	# return results
	# return render_template('index.html',results=results)

