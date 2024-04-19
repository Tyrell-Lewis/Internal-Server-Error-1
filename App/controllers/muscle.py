
from App.models import muscle
from App.database import db
from flask import request, jsonify

import requests #added requests library to requirements.txt to allow for outbound request calls to api.
import re



def get_all_muscles():
    
    return muscle.query.all()

def get_all_muscles_api():
    url = f'https://wger.de/api/v2/muscle/'
    
    response = requests.get(url)
   
    if response.status_code == 200:
        muscle_data = response.json().get('results', [])

        


        for muscle_d in muscle_data:
            
                name = muscle_d.get('name', '')
                name_en = muscle_d.get('name_en', '')
                musc_id = muscle_d.get('id')


                existing_id_muscle = muscle.query.filter_by(musc_id=musc_id).first()
                existing_name_muscle = muscle.query.filter_by(name=name).first()
                existing_name_en_muscle = muscle.query.filter_by(name_en=name_en).first()

                if existing_id_muscle or existing_name_muscle or existing_name_en_muscle:
                    pass
                else:

                    

                    n_muscle = muscle(musc_id=musc_id, name=name, name_en=name_en)
                    
                    db.session.add(n_muscle)
        db.session.commit()
        #return exercise_data
        
        return get_all_muscles()
    else:
        return None