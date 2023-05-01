"""order.py holding my parcel order views"""
from flask import Blueprint, jsonify, request
from api.models.models import Acquisitions
# from api.Helpers.validations import Validation
# from api.Helpers.error_handlers import InvalidUsage
# from api.models.auth import Users
# from flask_jwt_extended import (jwt_required, get_jwt_identity)
# from flasgger import swag_from

acquisition = Acquisitions()
# val = Validation()

parcel_blueprint = Blueprint("acquisition", __name__)