from flask import Flask
from database import db, init_db
from models.health_log import User, HealthLog, Goal

app = Flask(__name__)
init_db(app)

# Register routes
from routes.health_routes import health_bp
app.register_blueprint(health_bp)

@app.route('/')
def home():
    return "FitTrack is running! 🚀"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("All tables created successfully!")
    app.run(debug=True)