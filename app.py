from flask import Flask, jsonify, request
from config import Config
from models.Mission import Mission
from routes.missions import missions_bp
from scripts.create_tables import create_tables
from scripts.fetch_denormalized_data import fetch_denormalized_data
from scripts.insert_data import insert_normalized_data

app = Flask(__name__)
app.config.from_object(Config)

# Uncomment this if you need to initialize your database
# data = fetch_denormalized_data()
# create_tables()
# insert_normalized_data(data)
app.register_blueprint(missions_bp, url_prefix='/api/mission')


if __name__ == '__main__':
    app.run(debug=True)
