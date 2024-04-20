# from App.database import db
# from .user import *
# from .exercise import *

# class Workout(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     name = db.Column(db.String(500), nullable = False)
#     exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.exercise_api_id'))

#     def __init__(self, user_id, name, exercise_id):
#         self.user_id = user_id
#         self.name = name
#         self.exercise_id = exercise_id

from App.database import db
from App.models.exercise import exercise


workout_exercise = db.Table(
    'workout_exercise',
    db.Column('exercise_api_id', db.Integer, db.ForeignKey('exercise.exercise_api_id'), primary_key=True),
    db.Column('workout_id', db.Integer, db.ForeignKey('workout.work_id'), primary_key=True)
)

class workout(db.Model):

    work_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), nullable=True)
    description = db.Column(db.String(5000), nullable=True)
    sets = db.Column(db.Integer, nullable=True)
    reps = db.Column(db.Integer, nullable=True)

    
    exercise = db.relationship('exercise', secondary=workout_exercise, backref=db.backref('workouts', lazy='dynamic'))


    def __init__(self, work_id, name, description, sets, reps):
        self.work_id = work_id
        self.name = name
        self.description = description
        self.sets = sets
        self.reps = reps
        