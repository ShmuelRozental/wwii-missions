from app import db
from models.Location import Location
from models.Coordinates import Coordinates




class TargetDetails(db.Model):
    __tablename__ = 'target_details'
    target_id = db.Column(db.Integer, primary_key=True)
    target_type = db.Column(db.String(100), nullable=False)
    target_industry = db.Column(db.String(255), nullable=False)
    target_priority = db.Column(db.String(5), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('location.location_id'))
    coordinates_id = db.Column(db.Integer, db.ForeignKey('coordinates.coordinates_id'))

    location = db.relationship('Location', back_populates='targets')
    coordinates = db.relationship('Coordinates', back_populates='targets')



    def __repr__(self):
        return f"<TargetDetails {self.target_type}>"

    def to_dict(self):
        return {
            'target_id': self.target_id,
            'target_type': self.target_type,
            'target_industry': self.target_industry,
            'target_priority': self.target_priority,
            'location_id': self.location_id,
            'coordinates_id': self.coordinates_id,
            'location': self.location.to_dict() if self.location else None,
            'coordinates': self.coordinates.to_dict() if self.coordinates else None,
        }