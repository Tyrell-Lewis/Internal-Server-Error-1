from App.models import exercise
from App.models import equipment
from App.models import muscle
#from App.models import category
# from App.models import category
from App.database import db
from flask import request, jsonify

import requests #added requests library to requirements.txt to allow for outbound request calls to api.
import re


def get_all_exercises():
    return exercise.query.all()

def get_exercise(id):
    return exercise.query.filter_by(exercise_api_id=id).first()


def remove_html_tags(text):
    # Code sourced from online to clean the text in api, which contained html tags.
    html_tags_pattern = re.compile(r'<[^>]+>')

    nbsp_pattern = re.compile(r'&nbsp;')
    
    clean_text = re.sub(html_tags_pattern, '', text)
    clean_text = re.sub(nbsp_pattern, '', clean_text)
    return clean_text


def create_exercise(exercise_api_id, name, description):
    new_exercise= exercise(exercise_api_id=exercise_api_id, name=name, description=description) #cat_name=cat_name)
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
    

    if response.status_code == 200:
        exercise_data = response.json().get('results', [])



        for exercise_d in exercise_data:
            if exercise_d.get('language', {}).get('short_name') == 'en' or exercise_d.get('language', {}).get('id') == 2 or exercise_d.get('language', {}).get('full_name') == 'English':
                name = exercise_d.get('name', '')
                description = exercise_d.get('description', '')
                
                exercise_api_id = exercise_d.get('id')
                category_id = exercise_d.get('category', {}).get('id')
                
                muscles = exercise_d.get('muscles', [])
                muscle_ids = [muscle.get('id') for muscle in muscles]

                muscles2 = exercise_d.get('muscles_secondary', [])
                muscle_ids_2 = [muscle2.get('id') for muscle2 in muscles2]

                # muscle_id = muscle_id[0] if muscle_id else None
                # muscle_id_2 = muscle_id_2[0] if muscle_id_2 else None

                equipment_data = exercise_d.get('equipment', [])
                equipment_ids = [equipment.get('id') for equipment in equipment_data]

                
                
                #print (equipment_ids)


                existing_id_exercise = exercise.query.filter_by(exercise_api_id=exercise_api_id).first()
                existing_name_exercise = exercise.query.filter_by(name=name).first()

                if existing_id_exercise or existing_name_exercise:
                    pass
                else:

                    html_text = description
                    clean_text = remove_html_tags(html_text)
                    
                    n_exercise = exercise(exercise_api_id=exercise_api_id, name=name, description=clean_text, category_id=category_id)#, muscle_id=muscle_id, muscle_id_2=muscle_id_2)

                    db.session.add(n_exercise)

                    for equipment_id in equipment_ids:
                        
                        n_equipment = equipment.query.filter_by(equip_id=equipment_id).first()
                        
                        if n_equipment:
                            n_exercise.equipment.append(n_equipment)
                    
                    for muscle_id in muscle_ids:
                        
                        n_muscle = muscle.query.filter_by(musc_id=muscle_id).first()
                        
                        if n_muscle:
                            n_exercise.muscle.append(n_muscle)

                    for muscle_id_2 in muscle_ids_2:
                        
                        n_muscle_2 = muscle.query.filter_by(musc_id=muscle_id_2).first()
                        
                        if n_muscle_2:
                            n_exercise.muscle_2.append(n_muscle_2)

                            
                    
                    db.session.add(n_exercise)
        db.session.commit()
        #return exercise_data

        
        
        return get_all_exercises()
    else:
        return None

def getCategoryExercises(category_id):
    return exercise.query.filter_by(category_id = category_id).all()
