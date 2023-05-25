from flask import Blueprint
from .config import swagger_blueprint


swagger_bp = Blueprint('swagger', __name__)
