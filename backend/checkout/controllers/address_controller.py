# Epic Title: Address Entry in Checkout Process

from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from backend.checkout.models.address import Address
from backend.checkout.services.address_service import AddressService

address_bp = Blueprint('address', __name__)

@address_bp.route('/save-address', methods=['POST'])
def save_address():
    try:
        address_data = request.json
        address = Address(**address_data)
        result = AddressService.save_address(address)
        if result:
            return jsonify({"message": "Address saved successfully"}), 200
        else:
            return jsonify({"error": "Error saving address"}), 500
    except ValidationError as e:
        return jsonify({"errors": e.errors()}), 400