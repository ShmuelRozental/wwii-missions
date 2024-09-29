from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config
from db.connection import get_db_connection, close_db_connection

from scripts.create_tables import create_tables
from scripts.fetch_denormalized_data import fetch_denormalized_data
from scripts.insert_data import insert_normalized_data
from utils.create_mission_table import create_mission_tables

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    with app.app_context():
        create_mission_tables()
        # create_tables()
        # data = fetch_denormalized_data()
        # insert_normalized_data(data)

        db.init_app(app)
        migrate = Migrate(app, db)

    from routes.missions import missions_bp

    app.register_blueprint(missions_bp, url_prefix='/api/mission')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
