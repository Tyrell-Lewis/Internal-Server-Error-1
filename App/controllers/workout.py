from App.models import Workout
from App.database import db

def get_all_workouts():
    return Workout.query.all()

def create_workout(name, description):
    new_workout= Workout(name=name, description=description)
    db.session.add(new_workout)
    db.session.commit()
    return new_workout