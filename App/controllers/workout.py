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


def add_exer_to_workout(work_id, name, description, sets, reps):
    # new_exer = getExercise(exercise_api_id)

    # if new_exer:
    #     db.session.add(new_exer)
    #     db.session.commit()
    #     return new_exer
    # else:
    #     return None

    new_exercise= workout(work_id=work_id, name=name, description=description, sets=sets, reps=reps) #cat_name=cat_name)
    db.session.add(new_exercise)
    db.session.commit()
    return new_exercise

