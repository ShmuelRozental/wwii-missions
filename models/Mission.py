
from app import db
from models.TargetDetails import TargetDetails

class Mission(db.Model):
    __tablename__ = 'mission'
    mission_id = db.Column(db.Integer, primary_key=True)
    mission_date = db.Column(db.Date, nullable=True)
    theater_of_operations = db.Column(db.String(100), nullable=True)
    country = db.Column(db.String(100), nullable=True)
    air_force = db.Column(db.String(100), nullable=True)
    unit_id = db.Column(db.String(100), nullable=True)
    aircraft_series = db.Column(db.String(100), nullable=True)
    callsign = db.Column(db.String(100), nullable=True)
    mission_type = db.Column(db.String(100), nullable=True)
    takeoff_base = db.Column(db.String(255), nullable=True)
    takeoff_location = db.Column(db.String(255), nullable=True)
    takeoff_latitude = db.Column(db.String(15), nullable=True)
    takeoff_longitude = db.Column(db.Numeric(10, 6), nullable=True)
    target_id = db.Column(db.Integer, db.ForeignKey('target_details.target_id'))
    altitude_hundreds_of_feet = db.Column(db.Numeric(7, 2), nullable=True)
    airborne_aircraft = db.Column(db.Numeric(4, 1), nullable=True)
    attacking_aircraft = db.Column(db.Integer, nullable=True)
    bombing_aircraft = db.Column(db.Integer, nullable=True)
    aircraft_returned = db.Column(db.Integer, nullable=True)
    aircraft_failed = db.Column(db.Integer, nullable=True)
    aircraft_damaged = db.Column(db.Integer, nullable=True)
    aircraft_lost = db.Column(db.Integer, nullable=True)
    high_explosives = db.Column(db.String(255), nullable=True)
    high_explosives_type = db.Column(db.String(255), nullable=True)
    high_explosives_weight_pounds = db.Column(db.String(25), nullable=True)
    high_explosives_weight_tons = db.Column(db.Numeric(10, 2), nullable=True)
    incendiary_devices = db.Column(db.String(255), nullable=True)
    incendiary_devices_type = db.Column(db.String(255), nullable=True)
    incendiary_devices_weight_pounds = db.Column(db.Numeric(10, 2), nullable=True)
    incendiary_devices_weight_tons = db.Column(db.Numeric(10, 2), nullable=True)
    fragmentation_devices = db.Column(db.String(255), nullable=True)
    fragmentation_devices_type = db.Column(db.String(255), nullable=True)
    fragmentation_devices_weight_pounds = db.Column(db.Numeric(10, 2), nullable=True)
    fragmentation_devices_weight_tons = db.Column(db.Numeric(10, 2), nullable=True)
    total_weight_pounds = db.Column(db.Numeric(10, 2), nullable=True)
    total_weight_tons = db.Column(db.Numeric(10, 2), nullable=True)
    time_over_target = db.Column(db.String(8), nullable=True)
    bomb_damage_assessment = db.Column(db.String(255), nullable=True)
    source_id = db.Column(db.String(100), nullable=True)

    target_details = db.relationship('TargetDetails', backref='missions')

    def __repr__(self):
        return f"<Mission {self.mission_id}>"

    def to_dict(self):
        return {
            'mission_id': self.mission_id,
            'mission_date': self.mission_date,
            'theater_of_operations': self.theater_of_operations,
            'country': self.country,
            'air_force': self.air_force,
            'unit_id': self.unit_id,
            'aircraft_series': self.aircraft_series,
            'callsign': self.callsign,
            'mission_type': self.mission_type,
            'takeoff_base': self.takeoff_base,
            'takeoff_location': self.takeoff_location,
            'takeoff_latitude': self.takeoff_latitude,
            'takeoff_longitude': self.takeoff_longitude,
            'target_id': self.target_id,
            'altitude_hundreds_of_feet': self.altitude_hundreds_of_feet,
            'airborne_aircraft': self.airborne_aircraft,
            'attacking_aircraft': self.attacking_aircraft,
            'bombing_aircraft': self.bombing_aircraft,
            'aircraft_returned': self.aircraft_returned,
            'aircraft_failed': self.aircraft_failed,
            'aircraft_damaged': self.aircraft_damaged,
            'aircraft_lost': self.aircraft_lost,
            'high_explosives': self.high_explosives,
            'high_explosives_type': self.high_explosives_type,
            'high_explosives_weight_pounds': self.high_explosives_weight_pounds,
            'high_explosives_weight_tons': self.high_explosives_weight_tons,
            'incendiary_devices': self.incendiary_devices,
            'incendiary_devices_type': self.incendiary_devices_type,
            'incendiary_devices_weight_pounds': self.incendiary_devices_weight_pounds,
            'incendiary_devices_weight_tons': self.incendiary_devices_weight_tons,
            'fragmentation_devices': self.fragmentation_devices,
            'fragmentation_devices_type': self.fragmentation_devices_type,
            'fragmentation_devices_weight_pounds': self.fragmentation_devices_weight_pounds,
            'fragmentation_devices_weight_tons': self.fragmentation_devices_weight_tons,
            'total_weight_pounds': self.total_weight_pounds,
            'total_weight_tons': self.total_weight_tons,
            'time_over_target': self.time_over_target,
            'bomb_damage_assessment': self.bomb_damage_assessment,
            'source_id': self.source_id,
            'target_details': self.target_details.to_dict() if self.target_details else None
        }
