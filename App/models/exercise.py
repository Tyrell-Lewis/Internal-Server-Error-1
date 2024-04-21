from App.database import db
from App.models.category import category
from App.models.muscle import muscle
from App.models.equipment import equipment

exercise_equipment = db.Table(
    'exercise_equipment',
    db.Column('exercise_api_id', db.Integer, db.ForeignKey('exercise.exercise_api_id'), primary_key=True),
    db.Column('equipment_id', db.Integer, db.ForeignKey('equipment.equip_id'), primary_key=True)
)

exercise_muscle = db.Table(
    'exercise_muscle',
    db.Column('exercise_api_id', db.Integer, db.ForeignKey('exercise.exercise_api_id'), primary_key=True),
    db.Column('muscle_id', db.Integer, db.ForeignKey('muscle.musc_id'), primary_key=True)
)

exercise_muscle_2 = db.Table(
    'exercise_muscle_2',
    db.Column('exercise_api_id', db.Integer, db.ForeignKey('exercise.exercise_api_id'), primary_key=True),
    db.Column('muscle_id_2', db.Integer, db.ForeignKey('muscle.musc_id'), primary_key=True)
)



class exercise(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    exercise_api_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)
    description = db.Column(db.String(5000), nullable=False)
   
    
    
    category = db.relationship('category', backref=db.backref('exercise', lazy=True))
    category_id = db.Column(db.Integer, db.ForeignKey('category.cat_id'))
    
  
    
    equipment = db.relationship('equipment', secondary=exercise_equipment, backref=db.backref('exercises', lazy='dynamic'))
    muscle = db.relationship('muscle', secondary=exercise_muscle, backref=db.backref('exercises', lazy='dynamic'))
    muscle_2 = db.relationship('muscle', secondary=exercise_muscle_2, backref=db.backref('exercises_secondary', lazy='dynamic'))

    def __init__(self, exercise_api_id, name, description, category_id):# muscle_id, muscle_id_2):
        self.exercise_api_id = exercise_api_id
        self.name = name
        self.description = description
        #self.cat_name = cat_name
        self.category_id = category_id
        
        

    def __repr__(self):
        return ("exercise: {{self.name}}")

    def get_exercises_for_page(cls, page_number, limit):
        start_point = (page_number - 1) * limit
        return cls.query.offset(start_point).limit(limit).all()

    def search_exercises(self, page):
        matching_exercises = exercise.query
        return matching_exercises.paginate(page=page, per_page=20)

  