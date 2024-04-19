from App.database import db
from .user import *
from .exercise import *

class Workout(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(500), nullable = False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.exercise_api_id'))

    def __init__(self, user_id, name, exercise_id):
        self.user_id = user_id
        self.name = name
        self.exercise_id = exercise_id
