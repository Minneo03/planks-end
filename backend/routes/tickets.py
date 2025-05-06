from flask import Blueprint, jsonify

tickets_bp = Blueprint('tickets', __name__)

@tickets_bp.route('/')
def get_tickets():
    return jsonify([
        {"type": "General Admission", "price": 39.99},
        {"type": "Fast Pass", "price": 59.99},
    ])
