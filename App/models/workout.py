
from App.database import db
from App.models.workout_exercise import workout_exercise



workout_exercise_final = db.Table(
    'workout_exercise_final',
    db.Column('work_exer_id', db.Integer, db.ForeignKey('workout_exercise.work_exer_id'), primary_key=True),
    db.Column('work_id', db.Integer, db.ForeignKey('workout.work_id'), primary_key=True)
)

class workout(db.Model):

    work_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), nullable=True)
    description = db.Column(db.String(5000), nullable=True)
    # sets = db.Column(db.Integer, nullable=True)
    # reps = db.Column(db.Integer, nullable=True)
    exercise_id = db.Column(db.Integer, nullable=True)
    #user_id = db.Column(db.Integer, nullable=True)


    
    sets_reps = db.relationship('workout_exercise', secondary=workout_exercise_final, backref=db.backref('workouts', lazy='dynamic'))


    def __init__(self, name, description, exercise_id):
        #self.work_id = work_id
        self.name = name
        self.description = description
        # self.sets = sets
        # self.reps = reps
        self.exercise_id = exercise_id
        #self.user_id = user_id
        