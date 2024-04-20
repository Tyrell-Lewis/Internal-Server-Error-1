from App.models import workout
from App.models import exercise
from App.models import workout_exercise
from App.database import db

def get_all_workouts():
    return workout.query.all()

def get_test():
    return workout_exercise.query.all()
    #return db.session.query(workout_exercise).filter_by(work_id=1).all()



def create_workout(name, description, exercise_api_id):
   

    new_workout= workout(name=name, description=description, exercise_id=exercise_api_id) 

    #for equipment_id in equipment_ids:
    # db.session.add(new_workout)
    # db.session.commit()
    # return new_workout
                        
    exercise_instance = exercise.query.filter_by(exercise_api_id=exercise_api_id).first()
                        
    # if exercise_instance:
    #     new_workout.sets_reps.exercise.append(exercise_instance)
        
    #     # new_workout_exercise = workout_exercise(exercise_id=exercise_instance.exercise_api_id, sets=None, reps=None)
    #     # new_workout.sets_reps.append(new_workout_exercise)
        
    #     db.session.add(new_workout)
    #     db.session.commit()
    #     return new_workout
    # else:
    #     return None

    if exercise_instance:
        new_workout_exercise = workout_exercise(sets=None, reps=None, exercise_id=exercise_instance.exercise_api_id)
        new_workout.sets_reps.append(new_workout_exercise)
        db.session.add(new_workout)
        db.session.commit()
        return new_workout
    else:
        return None


def add_exer_to_workout(work_id, exercise_api_id, sets, reps):
    
    existing_workout= workout.query.get(work_id)
    #existing_workout_exercise = workout_exercise.query.get()

    if existing_workout:

        exercise_instance = exercise.query.filter_by(exercise_api_id=exercise_api_id).first()

        # if exercise_instance:

        #     new_workout_exercise = workout_exercise(work_id=existing_workout.work_id, exercise_api_id=exercise_instance.exercise_api_id, sets=sets, reps=reps)
        #     # Append the exercise to the existing workout's list of exercises
        #     existing_workout.exercise.append(exercise_instance)
        #     # existing_workout_exercise = db.session.query(workout_exercise).filter_by(work_id=work_id, exercise_api_id=exercise_api_id).first()
        #     # existing_workout_exercise.sets = sets
        #     # existing_workout_exercise.reps = reps
        #     existing_workout.workout_exercise.append(new_workout_exercise)
        #     #db.session.add(existing_workout_exercise)
        #     db.session.add(existing_workout)
        #     db.session.commit()
        #     return existing_workout
        # else:
            
        #     return None

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



