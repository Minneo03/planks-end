from flask import Blueprint, jsonify

amusements_bp = Blueprint('amusements', __name__)

@amusements_bp.route('/')
def get_amusements():
    return jsonify([
        {"name": "Pirate Plunge", "type": "Water Ride"},
        {"name": "Cannon Coaster", "type": "Roller Coaster"}
    ])
