from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class Mission(db.Model):
    __tablename__ = 'mission'
    mission_id = db.Column(db.Integer, primary_key=True)
    target_id = db.Column(db.Integer, db.ForeignKey('target_details.target_id'))

    target = db.relationship('TargetDetails', backref='missions')

    def __repr__(self):
        return f"<Mission {self.mission_id}>"