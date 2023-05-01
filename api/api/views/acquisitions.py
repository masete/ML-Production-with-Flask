"""order.py holding my parcel order views"""
from flask import Blueprint, jsonify, request
from api.models.models import Acquisitions

acquisition = Acquisitions()
# val = Validation()

acquisition_blueprint = Blueprint("acquisition", __name__)


@acquisition_blueprint.route('/api/v1/acquisition', methods=['GET'], strict_slashes=False)
# @jwt_required
def get_all_acquisitions():
    """
    endpoint to get all acquisition 
    :return:
    """
    # user_id = get_jwt_identity()

    acq = acquisition.get_all_acquisitions()
    return jsonify({"acquisition": acq})
