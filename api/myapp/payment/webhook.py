from flask import jsonify, request, Blueprint, redirect
from flask_cors import cross_origin
import hashlib


# paddle.api_key = 'YOUR_PADDLE_VENDOR_API_KEY'
webhook = Blueprint("webhook", __name__)

@webhook.route('/webhook', methods=['POST'])
@cross_origin()
def handle_webhook():
    payload = request.get_json()
    signature = request.headers.get('X-Paddle-Signature')
    vendor_api_key = 'YOUR_PADDLE_VENDOR_API_KEY'
    generated_signature = hashlib.sha1(payload + vendor_api_key.encode()).hexdigest()

    if signature != generated_signature:
        return 'Invalid signature', 400

    # Signature is valid, process the webhook payload
    event_type = payload['alert_name']
    if event_type == 'payment_succeeded':
        # Payment succeeded, generate access code/token for the user
        # Associate the access code/token with the user's purchase
        # Perform any additional actions based on the successful payment

    # Handle other event types as per your requirements

        return 'Webhook received', 200
