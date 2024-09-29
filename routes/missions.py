from flask import Blueprint, jsonify, request
from models.Mission import Mission

# Create a Blueprint
missions_bp = Blueprint('missions', __name__)

@missions_bp.route('/', methods=['GET'])
def get_missions():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    # Optional: Set a maximum limit for per_page
    max_per_page = 100
    if per_page > max_per_page:
        per_page = max_per_page

    try:
        # Use paginate with keyword arguments
        missions = Mission.query.paginate(page=page, per_page=per_page, error_out=False)
        return jsonify({
            'total': missions.total,
            'pages': missions.pages,
            'current_page': missions.page,
            'missions': [mission.to_dict() for mission in missions.items]  # Assuming you have a to_dict method
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Internal Server Error

@missions_bp.route('/<int:id>', methods=['GET'])
def get_mission(id):
    try:
        mission = Mission.query.get(id)
        if mission:
            return jsonify(mission.to_dict())  # Serialize the whole mission object
        return jsonify({'error': 'Mission not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Internal Server Error
