from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user

from.index import index_views

from App.controllers import (get_all_workouts, create_workout)

workout_views = Blueprint('workout_views', __name__, template_folder='../templates')

@workout_views.route('/workouts', methods=['GET'])
def get_workout_page():
    workouts = get_all_workouts()
    return render_template('workouts.html', workouts=workouts)

@workout_views.route('/workouts', methods=['POST'])
def create_workout_action():
    create_workout(request.form.get('workout_name'), request.form.get('workout_desc') )
    return redirect (url_for('workout_views.get_workout_page'))

