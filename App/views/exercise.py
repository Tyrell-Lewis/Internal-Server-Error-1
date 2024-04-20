from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user

from.index import index_views

from App.controllers import (get_all_exercises, create_exercise, get_all_exercises_api, get_all_categories, get_all_categories_api, get_all_muscles, get_all_muscles_api, get_all_equipment, get_all_equipment_api)

exercise_views = Blueprint('exercise_views', __name__, template_folder='../templates')

@exercise_views.route('/exercises', methods=['GET'])
def get_exercise_page():
    #exercises = get_all_exercises()
    # start_point = request.form.get('start_point')
    # limit = request.form.get('limit')

    start_point = 0 #This is starting point for all exercies
    limit = 200 #This gives the limit of how much exercises to render.

    #Just make sure the other models are populated first then call the exercise to do the functions.
    categories = get_all_categories_api()
    muscles = get_all_muscles_api()
    equipment = get_all_equipment_api()

    exercises = get_all_exercises_api(limit,start_point) #THIS SHOULD LOAD ON STARTUP, OR FIND A WAY TO POPULATE MODEL ON STARTUP
    
    #exercises = get_all_exercises()

    return render_template('exercises.html', exercises=exercises, categories=categories, muscles=muscles, equipment=equipment)

@exercise_views.route('/exercises', methods=['POST'])
def create_exercise_action():
    create_exercise(145, request.form.get('exercise_name'), request.form.get('exercise_desc'), 'Abs')# put a form method with options to choose from a list of categories
    return redirect (url_for('exercise_views.get_exercise_page'))
    #return redirect (request.referrer)

