from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user #as jwt_current_user

from .index import index_views

from App.controllers import (get_all_workouts,
                             create_workout,
                             add_exer_to_workout, 
                             get_workout_exercises, 
                             get_exercise, 
                             get_workout, 
                             delete_workout, 
                             delete_workout_exercise,
                             edit_workout_exercise)

workout_views = Blueprint('workout_views', __name__, template_folder='../templates')


@workout_views.route('/workouts', methods =['GET'])
@workout_views.route('/workouts/<id>', methods =['GET'])
@jwt_required()
def get_workout_page(id=None):
    workouts = get_all_workouts()
    workout_exercises = get_workout_exercises()
    sel_exercise = None
    if id:
        sel_exercise = get_exercise(id)
    return render_template('workouts.html', workouts = workouts, workout_exercises=workout_exercises, sel_exercise=sel_exercise, current_user=current_user)


@workout_views.route('/workouts/info', methods=['GET'])
@workout_views.route('/workouts/info/<id>', methods=['GET'])
@jwt_required()
def get_workout_info_page(id=None):
    workouts = get_all_workouts()
    workout_exercises = get_workout_exercises()
    sel_workout = None
    if id:
        sel_workout = get_workout(id)
    return render_template('workout.html', workouts = workouts, workout_exercises=workout_exercises, sel_workout=sel_workout, current_user=current_user)


@workout_views.route('/workouts', methods=['POST'])
@jwt_required()
def create_workout_action():
    create_workout(request.form.get('name'), request.form.get('desc'), 0, current_user.id)
    return redirect (url_for('workout_views.get_workout_page'))


@workout_views.route('/workouts/add', methods=['POST'])
@jwt_required()
def add_workout_exercise():
    exercise_id = request.form.get('exercise_id')
    workout_id = request.form.get('workout_id')
    sets = request.form.get('sets')
    reps = request.form.get('reps')
    add_exer_to_workout(workout_id, exercise_id, sets, reps)
    return redirect (url_for('workout_views.get_workout_page'))


@workout_views.route('/workouts/edit', methods=['POST'])
@workout_views.route('/workouts/edit/<wid>/<eid>', methods=['POST'])
@jwt_required()
def edit_workout_action(wid=None, eid=None):
    data = request.form
    sets = data['sets']
    reps = data['reps']

    edit_workout_exercise(wid, eid, sets, reps)

    sel_workout = None
    if wid:
        sel_workout = get_workout(wid)

    return render_template('workout.html',  sel_workout=sel_workout, current_user=current_user)


@workout_views.route('/workouts/info/edit', methods=['GET'])
@workout_views.route('/workouts/info/edit/<wid>/<eid>', methods=['GET'])
@jwt_required()
def test(wid=None, eid=None):
    btn_click=True
    sel_workout = None

    sel_exercise = get_exercise(eid)

    if wid:
        sel_workout = get_workout(wid)
    return render_template('workout.html',  sel_workout=sel_workout, current_user=current_user, btn_click=btn_click, sel_exercise=sel_exercise)


@workout_views.route('/workouts/delete', methods=['GET'])
@workout_views.route('/workouts/delete/<id>', methods=['GET'])
@jwt_required()
def delete_workout_action(id=None):
    if id:
        delete_workout(id)
    # return redirect(url_for('workout_views.get_workout_page'))
    return redirect(request.referrer)


@workout_views.route('/workouts/info/delete', methods=['GET'])
@workout_views.route('/workouts/info/delete/<wid>/<eid>', methods=['GET'])
@jwt_required()
def delete_workout_exercise_action(wid=None, eid=None):
    if wid:
        if eid:
            delete_workout_exercise(wid, eid)
    # return redirect(url_for('workout_views.get_workout_page'))
    return redirect(request.referrer)

