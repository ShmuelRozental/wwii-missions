from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class TargetDetails(db.Model):
    __tablename__ = 'target_details'
    target_id = db.Column(db.Integer, primary_key=True)
    target_type = db.Column(db.String(100), nullable=False)
    target_industry = db.Column(db.String(255), nullable=False)
    target_priority = db.Column(db.String(5), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('location.location_id'))
    coordinates_id = db.Column(db.Integer, db.ForeignKey('coordinates.coordinates_id'))

    location = db.relationship('Location', backref='targets')
    coordinates = db.relationship('Coordinates', backref='targets')

    def __repr__(self):
        return f"<TargetDetails {self.target_type}>"
