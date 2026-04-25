from flask import Blueprint, request, jsonify
from database import db
from datetime import datetime
from models.health_log import User, HealthLog, Goal

health_bp = Blueprint('health', __name__)

# API 1: Add a new user
@health_bp.route('/user', methods=['POST'])
def add_user():
    data = request.json  # get data sent from the request

    new_user = User(
        name=data['name'],
        age=data['age'],
        gender=data['gender'],
        height_cm=data['height_cm'],
        weight_kg=data['weight_kg']
    )

    db.session.add(new_user)   # add to database session
    db.session.commit()         # save to database

    return jsonify({
        "message": "User added successfully!",
        "user_id": new_user.user_id
    }), 201
# API 2: Log daily health data
@health_bp.route('/log', methods=['POST'])
def log_health():
    data = request.json

    new_log = HealthLog(
        user_id=data['user_id'],
        date=datetime.strptime(data['date'], '%Y-%m-%d').date(),
        steps=data['steps'],
        calories_burned=data['calories_burned'],
        sleep_hours=data['sleep_hours'],
        heart_rate_avg=data['heart_rate_avg'],
        water_intake_liters=data['water_intake_liters']
    )

    db.session.add(new_log)
    db.session.commit()

    return jsonify({"message": "Health data logged successfully!"}), 201

    db.session.add(new_log)
    db.session.commit()

    return jsonify({"message": "Health data logged successfully!"}), 201
# API 3: Get all health logs of a user
@health_bp.route('/logs/<int:user_id>', methods=['GET'])
def get_logs(user_id):
    logs = HealthLog.query.filter_by(user_id=user_id).all()

    result = []
    for log in logs:
        result.append({
            "date": str(log.date),
            "steps": log.steps,
            "calories_burned": log.calories_burned,
            "sleep_hours": log.sleep_hours,
            "heart_rate_avg": log.heart_rate_avg,
            "water_intake_liters": log.water_intake_liters
        })

    return jsonify({"user_id": user_id, "logs": result}), 200
# API 4: Add a goal
@health_bp.route('/goal', methods=['POST'])
def add_goal():
    data = request.json

    new_goal = Goal(
        user_id=data['user_id'],
        goal_type=data['goal_type'],
        target_value=data['target_value'],
        start_date=datetime.strptime(data['start_date'], '%Y-%m-%d').date(),
        end_date=datetime.strptime(data['end_date'], '%Y-%m-%d').date()
    )

    db.session.add(new_goal)
    db.session.commit()

    return jsonify({"message": "Goal added successfully!"}), 201