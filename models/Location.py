from app import db

class Location(db.Model):
    __tablename__ = 'location'
    location_id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)

    targets = db.relationship('TargetDetails', back_populates='location')
    def __repr__(self):
        return f"<Location {self.city}, {self.country}>"

    def to_dict(self):
        return {
            'location_id': self.location_id,
            'country': self.country,
            'city': self.city,
        }