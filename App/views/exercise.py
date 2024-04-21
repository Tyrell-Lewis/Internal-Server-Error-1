from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user

from.index import index_views

from App.controllers import (get_all_exercises, create_exercise, get_all_exercises_api, get_all_categories, get_all_categories_api, get_all_muscles, get_all_muscles_api, get_all_equipment, get_all_equipment_api, getCategoryExercises)

exercise_views = Blueprint('exercise_views', __name__, template_folder='../templates')

@exercise_views.route('/exercises', methods=['GET'])
@exercise_views.route('/exercises/<int:cat_id>', methods=['GET'])
def get_exercise_page(cat_id = -1):
    #exercises = get_all_exercises()
    # start_point = request.form.get('start_point')
    # limit = request.form.get('limit')

    start_point = 0 #This is starting point for all exercies
    limit = 20 #This gives the limit of how much exercises to render.

    #Just make sure the other models are populated first then call the exercise to do the functions.
    category = get_all_categories()
    muscles = get_all_muscles()
    equipment = get_all_equipment()
    if cat_id == -1:
        exercises = get_all_exercises()#THIS SHOULD LOAD ON STARTUP, OR FIND A WAY TO POPULATE MODEL ON STARTUP
    else:
        exercises = getCategoryExercises(cat_id)

    
    
    #exercises = get_all_exercises()

    return render_template('exercises.html', exercises=exercises, category = category, muscles=muscles, equipment=equipment, exercise_id=request.args.get('exercise_id'))



