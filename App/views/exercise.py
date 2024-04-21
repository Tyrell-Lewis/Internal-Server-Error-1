from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user

from.index import index_views

import requests

from App.controllers import (get_all_exercises, calculate_total_pages ,get_exercises_from_database ,create_exercise, get_all_exercises_api, get_all_categories, get_all_categories_api, get_all_muscles, get_all_muscles_api, get_all_equipment, get_all_equipment_api, getCategoryExercises)

exercise_views = Blueprint('exercise_views', __name__, template_folder='../templates')

@exercise_views.route('/exercises', methods=['GET'])
@exercise_views.route('/exercises/<int:cat_id>', methods=['GET'])
def get_exercise_page(cat_id = -1):
    
    page = request.args.get('page', 1, type=int)
    limit = 20  # Number of exercises per page
    start_point = (page - 1) * limit
    

    exercises, total_pages = get_all_exercises_api(limit, start_point)

    category = get_all_categories()
    muscles = get_all_muscles()
    equipment = get_all_equipment()
    #exercise_data = get_all_exercises()
    if cat_id == -1:
        exercise_data = get_all_exercises()#THIS SHOULD LOAD ON STARTUP, OR FIND A WAY TO POPULATE MODEL ON STARTUP
    else:
        exercise_data = getCategoryExercises(cat_id)
        if exercise_data:
            pass
        else:
            flash('No Category Found!')

    

    return render_template('exercises.html', exercise_data=exercise_data, category=category, muscles=muscles, equipment=equipment, total_pages=total_pages, page=page, exercises=exercises)









