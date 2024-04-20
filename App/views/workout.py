from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user

from .index import index_views

from App.controllers import (get_all_workouts, add_exer_to_workout)

workout_views = Blueprint('workout_views', __name__, template_folder='../templates')

@workout_views.route('/workouts', methods =['GET'])
@jwt_required()
def get_workout_page():

    workouts = get_all_workouts()
    return render_template('workouts.html', workouts = workouts)


@workout_views.route('/workouts', methods=['POST'])
def create_workout_action():
    add_exer_to_workout(request.form.get('exer_id'), "The workout is working", 3, 10, 81)#this is just a temp to test that workout model is working
    #add_exer_to_workout(request.form.get('exer_id'), "The workout is still working", 4, 15, 74)
    return redirect (url_for('workout_views.get_workout_page'))
    #return redirect (request.referrer)
