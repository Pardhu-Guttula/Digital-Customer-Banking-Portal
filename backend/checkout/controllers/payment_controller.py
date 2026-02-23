# Epic Title: Payment Processing During Checkout

from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from backend.checkout.models.payment import Payment
from backend.checkout.services.payment_service import PaymentService

payment_bp = Blueprint('payment', __name__)

@payment_bp.route('/process-payment', methods=['POST'])
def process_payment():
    try:
        payment_data = request.json
        payment = Payment(**payment_data)
        result, message = PaymentService.process_payment(payment)
        if result:
            return jsonify({"message": "Payment processed successfully"}), 200
        else:
            return jsonify({"error": message}), 400
    except ValidationError as e:
        return jsonify({"errors": e.errors()}), 400