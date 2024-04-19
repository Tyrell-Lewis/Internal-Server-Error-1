from App.models import exercise
from App.database import db
from flask import request, jsonify

import requests #added requests library to requirements.txt to allow for outbound request calls to api.
import re


def get_all_exercises():
    return exercise.query.all()


def remove_html_tags(text):
    # Code sourced from online to clean the text in api, which contained html tags.
    html_tags_pattern = re.compile(r'<[^>]+>')

    nbsp_pattern = re.compile(r'&nbsp;')
    
    clean_text = re.sub(html_tags_pattern, '', text)
    clean_text = re.sub(nbsp_pattern, '', clean_text)
    return clean_text


def create_exercise(name, description, cat_name):
    new_exercise= exercise(name=name, description=description, cat_name=cat_name)
    db.session.add(new_exercise)
    db.session.commit()
    return new_exercise

def get_all_exercises_api(limit, start_point):
    url = f'https://wger.de/api/v2/exerciseinfo/?limit={limit}&offset={start_point}'
    #the limit=5 means it only renders the 5 at a time
    #the offset=0 means it starts from the 1st one, which is at 0 like an array list
    # can manipulate the url by using variable for the numbers {{}} or ${} whichever one works for this.
    #doing just https://wger.de/api/v2/exercise/ gives the default first 20 exercises, but should use the limit and offset to increment rhough different ones.

    #this works to get api data and works in views and template, but doesnt save data to model and database, finda  way to do this tmr.
    
    response = requests.get(url)
    # if response.status_code == 200:
    #     return response.json().get('results', [])
    # else:
    #     return None

    if response.status_code == 200:
        exercise_data = response.json().get('results', [])



        for exercise_d in exercise_data:
            if exercise_d.get('language', {}).get('short_name') == 'en' or exercise_d.get('language', {}).get('id') == 2 or exercise_d.get('language', {}).get('full_name') == 'English':
                name = exercise_d.get('name', '')
                description = exercise_d.get('description', '')
                cat_name = exercise_d.get('category', {}).get('name')

                existing_exercise = exercise.query.filter_by(name=name).first()

                if existing_exercise:
                    pass
                else:

                    html_text = description
                    clean_text = remove_html_tags(html_text)

                    n_exercise = exercise(name=name, description=clean_text, cat_name=cat_name)
                    db.session.add(n_exercise)
        db.session.commit()
        #return exercise_data
        return get_all_exercises()
    else:
        return None
