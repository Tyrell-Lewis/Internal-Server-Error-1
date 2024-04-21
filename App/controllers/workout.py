from App.models import workout
from App.models import exercise
from App.models import workout_exercise
from App.models import User
from App.database import db


def get_all_workouts():
    return workout.query.all()


def get_workout(id):
    return workout.query.filter_by(work_id=id).first()


def get_workout_exercises():
    return workout_exercise.query.all()
    #return db.session.query(workout_exercise).filter_by(work_id=1).all()


def create_workout(name, description, exercise_api_id, user_id):
    new_workout= workout(name=name, description=description, exercise_id=exercise_api_id) 

    if new_workout:
        existing_user = User.query.get(user_id)

        if existing_user:
            existing_user.workout.append(new_workout)
            db.session.add(new_workout)
            db.session.commit()
            return new_workout
        else:
            return None
    else:
        return None
 
                        
    # exercise_instance = exercise.query.filter_by(exercise_api_id=exercise_api_id).first()
    

    # if exercise_instance:
    #     new_workout_exercise = workout_exercise(sets=None, reps=None, exercise_id=exercise_instance.exercise_api_id)
    #     new_workout.sets_reps.append(new_workout_exercise)
    #     db.session.add(new_workout)
    #     db.session.commit()
    #     return new_workout
    # else:
    #     return None


def add_exer_to_workout(work_id, exercise_api_id, sets, reps):
    existing_workout= workout.query.get(work_id)
    #existing_workout_exercise = workout_exercise.query.get()

    if existing_workout:
        exercise_instance = exercise.query.filter_by(exercise_api_id=exercise_api_id).first()

        if exercise_instance:
            new_workout_exercise = workout_exercise(sets=sets, reps=reps, exercise_id=exercise_instance.exercise_api_id)
            new_workout_exercise.exercise.append(exercise_instance)
            db.session.add(new_workout_exercise)
            existing_workout.sets_reps.append(new_workout_exercise)
            db.session.add(existing_workout)
            db.session.commit()
            return existing_workout
        else:
            # If the exercise instance doesn't exist, return None
            return None
    else:
        None


def delete_workout(work_id):
    workout = get_workout(work_id)
    if workout:
        db.session.delete(workout)
        db.session.commit()
    else:
        return None


def delete_workout_exercise(work_id, exer_id):
    ex = exercise.query.filter_by(exercise_api_id=exer_id).first()
    existing_workout = workout.query.get(work_id)
    if existing_workout:
        exercise_instance = workout_exercise.query.filter_by(exercise_id=exer_id).first()
        if exercise_instance:
            exercise_instance.exercise.remove(ex)
            db.session.commit()
        else:
            return None
    else:
        return None

