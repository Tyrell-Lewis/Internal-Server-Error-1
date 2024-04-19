from App.models import Workout
from App.models import exercise
from App.database import db

def getAllWorkouts():
    return Workout.query.all()

def getExercise(id):
    return exercise.query.get(id)

def addExercise(user_id, name, exercise_id):
    newExercise = exercise(user_id, name, exercise_id)
    if newExercise:
        db.session.add(newExercise)
        db.session.commit()


