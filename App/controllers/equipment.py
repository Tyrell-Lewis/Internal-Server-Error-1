
from App.models import equipment
from App.database import db
from flask import request, jsonify

import requests #added requests library to requirements.txt to allow for outbound request calls to api.
import re



def get_all_equipment():
    
    return equipment.query.all()

def get_all_equipment_api():
    url = f'https://wger.de/api/v2/equipment/'
    
    response = requests.get(url)
   
    if response.status_code == 200:
        equipment_data = response.json().get('results', [])

        


        for equipment_d in equipment_data:
            
                name = equipment_d.get('name', '')
                
                equip_id = equipment_d.get('id')

                


                existing_id_equipment = equipment.query.filter_by(equip_id=equip_id).first()
                existing_name_equipment= equipment.query.filter_by(name=name).first()

                if existing_id_equipment or existing_name_equipment:
                    pass
                else:

                    

                    n_equipment = equipment(equip_id=equip_id, name=name)
                    
                    db.session.add(n_equipment)
        db.session.commit()
        #return exercise_data
        
        return get_all_equipment()
    else:
        return None