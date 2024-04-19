
from App.models import category
from App.database import db
from flask import request, jsonify

import requests #added requests library to requirements.txt to allow for outbound request calls to api.
import re



def get_all_categories():
    
    return category.query.all()

def get_all_categories_api():
    url = f'https://wger.de/api/v2/exercisecategory/'
    
    response = requests.get(url)
   
    if response.status_code == 200:
        category_data = response.json().get('results', [])

        


        for category_d in category_data:
            
                name = category_d.get('name', '')
                
                cat_id = category_d.get('id')

                


                existing_id_category = category.query.filter_by(cat_id=cat_id).first()
                existing_name_category= category.query.filter_by(name=name).first()

                if existing_id_category or existing_name_category:
                    pass
                else:

                    

                    n_category = category(cat_id=cat_id, name=name)
                    
                    db.session.add(n_category)
        db.session.commit()
        #return exercise_data
        
        return get_all_categories()
    else:
        return None