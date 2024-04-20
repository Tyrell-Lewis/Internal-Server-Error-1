from App.database import db
from App.models.exercise import exercise

sets_exercise = db.Table(
    'sets_exercise',
    db.Column('exercise_api_id', db.Integer, db.ForeignKey('exercise.exercise_api_id'), primary_key=True),
    db.Column('work_exer_id', db.Integer, db.ForeignKey('workout_exercise.work_exer_id'), primary_key=True)
    
)

class workout_exercise(db.Model):

    work_exer_id = db.Column(db.Integer, primary_key = True)
    # name = db.Column(db.String(120), nullable=True)
    # description = db.Column(db.String(5000), nullable=True)
    sets = db.Column(db.Integer, nullable=True)
    reps = db.Column(db.Integer, nullable=True)
    exercise_id = db.Column(db.Integer, nullable=False)

    
    exercise = db.relationship('exercise', secondary=sets_exercise, backref=db.backref('workout_exercises', lazy='dynamic'))


    def __init__(self, sets, reps, exercise_id):
        #self.work_id = work_id
        # self.name = name
        # self.description = description
        self.sets = sets
        self.reps = reps
        self.exercise_id=exercise_id
    
    