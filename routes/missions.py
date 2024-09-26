from flask import Blueprint, jsonify, request
from models.Mission import Mission

# Create a Blueprint
missions_bp = Blueprint('missions', __name__)

@missions_bp.route('/', methods=['GET'])
def get_missions():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    missions = Mission.query.paginate(page, per_page, error_out=False)
    return jsonify({
        'total': missions.total,
        'pages': missions.pages,
        'current_page': missions.page,
        'missions': [{'mission_id': mission.mission_id, 'target_id': mission.target_id} for mission in missions.items]
    })

@missions_bp.route('/<int:id>', methods=['GET'])
def get_mission(id):
    try:
        mission = Mission.query.get(id)
        if mission:
            return jsonify({
                'mission_id': mission.mission_id,
                'target_id': mission.target_id
            })
        return jsonify({'error': 'Mission not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Internal Server Error
