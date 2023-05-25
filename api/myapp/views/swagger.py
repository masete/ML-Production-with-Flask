from flask import Blueprint
from flasgger import Swagger

swagger_bp = Blueprint('swagger', __name__, url_prefix='/swagger')
swagger = Swagger(swagger_bp, template_file='swagger.yml')
