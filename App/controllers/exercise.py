from App.models import exercise
from App.database import db
from flask import request, jsonify

import requests



def get_all_exercises():
    return exercise.query.all()

def create_exercise(name, description):
    new_exercise= exercise(name=name, description=description)
    db.session.add(new_exercise)
    db.session.commit()
    return new_exercise

def get_all_exercises_api():
    url = 'https://wger.de/api/v2/exercise/'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        return None