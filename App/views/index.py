from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db
from App.controllers import (create_user, get_all_categories_api, get_all_equipment_api, get_all_exercises_api, get_all_muscles_api)

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    get_all_categories_api()
    get_all_muscles_api()
    get_all_equipment_api()
    return render_template('index.html')


@index_views.route('/home', methods=['GET'])
def home_page():
    return render_template('index.html')



@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()

    create_user('bob', 'bobpass', 'Trinidad', 'Male', 'CLX', 180, 157.6)
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})