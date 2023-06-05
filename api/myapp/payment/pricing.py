from flask import jsonify, request, Blueprint, redirect
from flask_cors import cross_origin
import stripe

# paddle.api_key = 'YOUR_PADDLE_VENDOR_API_KEY'
pricing = Blueprint("pricing", __name__)

stripe.api_key = 'YOUR_STRIPE_SECRET_KEY'


@pricing.route("/api/v1/pay", methods=['POST'])
@cross_origin()
def pay_for_resources():
    try:
        data = request.get_json()
        num_deals = data.get('num_deals')
        unit_cost = 0.001
        total_cost = num_deals * unit_cost

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product': 'YOUR_PRODUCT_ID',  # Replace with your Stripe product ID
                    'unit_amount': int(total_cost * 100),  # Amount in cents
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://yourdomain.com/success',
            cancel_url='http://yourdomain.com/cancel',
        )

        return jsonify({'checkout_url': session.url}), 200

    except stripe.error.StripeError:
        return jsonify({'error': 'Payment request failed.'}), 400

# Step 6: Verify the payment
# @pricing.route('/webhook', methods=['POST'])
# @cross_origin()
# def webhook():
#     payload = request.get_json()
#     event = None

#     try:
#         event = stripe.Event.construct_from(payload, stripe.api_key)
#     except ValueError as e:
#         return jsonify({'error': str(e)}), 400

#     # Handle the payment succeeded event
#     if event.type == 'checkout.session.completed':
#         session = event.data.object
#         # Retrieve the payment information and mark it as successful in your database

#     return jsonify({'success': True})

# Step 7: Provide access to the results
# @pricing.route('/results', methods=['GET'])
# @cross_origin()
# def results():
#     # Check if the payment is verified for the user making the request
#     # If the payment is verified, return the requested records
#     # Otherwise, return an error or redirect to the payment endpoint

#     # Example code for demonstration purposes only
#     # Replace with your own logic to verify the payment status
#     payment_verified = True

#     if payment_verified:
#         return jsonify({'data': 'Here are your results.'})
#     else:
#         return jsonify({'error': 'Payment not verified.'}), 401
