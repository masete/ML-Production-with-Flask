from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/api/docs'  # URL for accessing Swagger UI
API_URL = '/static/swagger.json'  # URL for accessing the OpenAPI JSON

# Create a Swagger blueprint
swagger_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Your Application Name"
    }
)
