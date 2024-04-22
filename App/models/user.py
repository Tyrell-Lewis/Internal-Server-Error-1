from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from App.models.workout import workout

user_workout = db.Table(
    'user_workout',
    db.Column('work_id', db.Integer, db.ForeignKey('workout.work_id'), primary_key=True),
    db.Column('users_ids', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    country = db.Column(db.String(120), nullable=True)
    gender = db.Column(db.String(120), nullable=True)
    gym = db.Column(db.String(120), nullable=True)
    height = db.Column(db.Integer, nullable=True)
    weight = db.Column(db.Float, nullable=True)

    


    workout = db.relationship('workout', secondary=user_workout, backref=db.backref('users', lazy='dynamic'))

    def __init__(self, username, password, country, gender, gym, height, weight):
        self.username = username
        self.set_password(password)
        self.country = country
        self.gender = gender
        self.gym = gym
        self.height = height
        self.weight = weight

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

