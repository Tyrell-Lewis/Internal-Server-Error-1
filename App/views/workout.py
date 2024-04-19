from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user

from .index import index_views

from App.controllers import (getAllWorkouts)

workout_views = Blueprint('workout_views', __name__, template_folder='../templates')

@workout_views.route('/workouts', methods =['GET'])
@jwt_required()
def getWorkoutPage():
    workouts = getAllWorkouts()
    return render_template('workouts.html', workouts = workouts)


    