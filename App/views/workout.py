from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user

from .index import index_views

from App.controllers import (get_all_workouts, create_workout, add_exer_to_workout, get_test)

workout_views = Blueprint('workout_views', __name__, template_folder='../templates')

@workout_views.route('/workouts', methods =['GET'])
@workout_views.route('/workouts/<int:ex_id', methods =['GET'])
@jwt_required()
def get_workout_page(ex_id):
    workouts = get_all_workouts()
    test = get_test()
    return render_template('workouts.html', workouts = workouts, test=test)


@workout_views.route('/workouts', methods=['POST'])
def create_workout_action():
    create_workout(request.form.get('exer_id'), "The workout is working", 81)#this is just a temp to test that workout model is working
    add_exer_to_workout(1, 74, 4, 15)#use forms to get data and make it dynamic
    add_exer_to_workout(1, 81, 500, 75)
    return redirect (url_for('workout_views.get_workout_page'))
    #return redirect (request.referrer)
