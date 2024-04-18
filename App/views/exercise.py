from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user

from.index import index_views

from App.controllers import (get_all_exercises, create_exercise, get_all_exercises_api)

exercise_views = Blueprint('exercise_views', __name__, template_folder='../templates')

@exercise_views.route('/exercises', methods=['GET'])
def get_exercise_page():
    #exercises = get_all_exercises()
    # start_point = request.form.get('start_point')
    # limit = request.form.get('limit')

    start_point = 0 #This is starting point for all exercies
    limit = 20 #This gives the limit of how much exercises to render.
    exercises = get_all_exercises_api(limit,start_point)
    #exercises = get_all_exercises()

    return render_template('exercises.html', exercises=exercises)

@exercise_views.route('/exercises', methods=['POST'])
def create_exercise_action():
    create_exercise(request.form.get('exercise_name'), request.form.get('exercise_desc') )
    return redirect (url_for('exercise_views.get_exercise_page'))
    #return redirect (request.referrer)

