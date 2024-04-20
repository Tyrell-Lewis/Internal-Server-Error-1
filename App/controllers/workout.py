from App.models import workout
from App.models import exercise
from App.database import db

def get_all_workouts():
    return workout.query.all()

def getExercise(exercise_api_id):
    return exercise.query.get(exercise_api_id=exercise_api_id)

def addExercise(user_id, name, exercise_id):
    newExercise = exercise(user_id, name, exercise_id)
    if newExercise:
        db.session.add(newExercise)
        db.session.commit()


def add_exer_to_workout(name, description, sets, reps, exer_id):
   

    new_exercise= workout(name=name, description=description, sets=sets, reps=reps) #cat_name=cat_name)

    #for equipment_id in equipment_ids:
                        
    n_equipment = exercise.query.filter_by(exercise_api_id=exer_id).first()
                        
    if n_equipment:
        new_exercise.exercise.append(n_equipment)
    db.session.add(new_exercise)
    db.session.commit()
    return new_exercise

