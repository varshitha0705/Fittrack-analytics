from database import db
from datetime import datetime

# Table 1: Users
class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    height_cm = db.Column(db.Float)
    weight_kg = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<User {self.name}>"


# Table 2: Health Logs
class HealthLog(db.Model):
    __tablename__ = 'health_logs'

    log_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    date = db.Column(db.Date)
    steps = db.Column(db.Integer)
    calories_burned = db.Column(db.Float)
    sleep_hours = db.Column(db.Float)
    heart_rate_avg = db.Column(db.Integer)
    water_intake_liters = db.Column(db.Float)
    logged_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<HealthLog user={self.user_id} date={self.date}>"


# Table 3: Goals
class Goal(db.Model):
    __tablename__ = 'goals'

    goal_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    goal_type = db.Column(db.String(50))  # e.g. 'steps', 'calories', 'sleep'
    target_value = db.Column(db.Float)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)

    def __repr__(self):
        return f"<Goal user={self.user_id} type={self.goal_type}>"