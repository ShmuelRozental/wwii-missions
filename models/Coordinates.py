from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Coordinates(db.Model):
    __tablename__ = 'coordinates'
    coordinates_id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Numeric(10, 6), nullable=False)
    longitude = db.Column(db.Numeric(10, 6), nullable=False)

    def __repr__(self):
        return f"<Coordinates ({self.latitude}, {self.longitude})>"
