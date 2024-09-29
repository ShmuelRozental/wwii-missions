from app import db

class Coordinates(db.Model):
    __tablename__ = 'coordinates'
    coordinates_id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Numeric(10, 6), nullable=False)
    longitude = db.Column(db.Numeric(10, 6), nullable=False)

    targets = db.relationship('TargetDetails', back_populates='coordinates')

    def __repr__(self):
        return f"<Coordinates ({self.latitude}, {self.longitude})>"

    def to_dict(self):
        return {
            'coordinates_id': self.coordinates_id,
            'latitude': str(self.latitude),
            'longitude': str(self.longitude)
        }