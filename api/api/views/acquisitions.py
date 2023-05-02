"""order.py holding my acquisition views"""

from flask import Blueprint

from ..__init__ import mysql


# hello = Blueprint('hello',__name__)
acquisition_blueprint = Blueprint("acquisition", __name__)


@acquisition_blueprint.route('/api/v1/acquisition', methods=['GET'], strict_slashes=False)
def get_all_acquisitions():

	
	c = mysql.db.cursor()
	c.execute('SELECT * FROM acquisition')
	results = c.fetchall()
	return results
	# return render_template('index.html',results=results)
# from flask import Blueprint, jsonify, request
# from flask_mysqldb import MySQL
# from api.models.models import Acquisitions

# acquisition = Acquisitions()
# val = Validation()

# acquisition_blueprint = Blueprint("acquisition", __name__)
# mysql = MySQL(acquisition_blueprint)

# @acquisition_blueprint.route('/api/v1/acquisition', methods=['GET'], strict_slashes=False)
# # @jwt_required
# def get_all_acquisitions():
#     """
#     endpoint to get all acquisition 
#     :return:
#     """
#     # user_id = get_jwt_identity()
#     cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#     cursor.execute('SELECT * FROM Acquisitions')
#     # Fetch one record and return result
#     acq = cursor.fetchall()

#     # acq = acquisition.get_all_acquisitions()
#     return jsonify({"acquisition": acq})
