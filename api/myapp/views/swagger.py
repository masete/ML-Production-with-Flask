from flask import render_template, Blueprint
from flask_cors import cross_origin

swagger_bp = Blueprint("swagger_bp", __name__)

@swagger_bp.route("/api/docs/")
@cross_origin()
def swagger_ui():
    return render_template("swagger_ui.html")
