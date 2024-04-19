from App.database import db
from App.models.category import category
from App.models.muscle import muscle
from App.models.equipment import equipment

exercise_equipment = db.Table(
    'exercise_equipment',
    db.Column('exercise_api_id', db.Integer, db.ForeignKey('exercise.exercise_api_id'), primary_key=True),
    db.Column('equipment_id', db.Integer, db.ForeignKey('equipment.equip_id'), primary_key=True)
)

class exercise(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    exercise_api_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)
    description = db.Column(db.String(5000), nullable=False)
    #cat_name = db.Column(db.String(120), nullable=False)
    
    # categories = db.relationship('category', backref=db.backref('exercises', lazy=True))
    # category_id = db.Column(db.Integer, db.ForeignKey('category.cat_id'), nullable=False)
    category = db.relationship('category', backref=db.backref('exercise', lazy=True))
    category_id = db.Column(db.Integer, db.ForeignKey('category.cat_id'))
    
    muscle_id = db.Column(db.Integer, db.ForeignKey('muscle.musc_id'))
    muscle = db.relationship('muscle', foreign_keys=[muscle_id], backref=db.backref('exercise', lazy=True))
    muscle_id_2 = db.Column(db.Integer, db.ForeignKey('muscle.musc_id'))
    muscle_2 = db.relationship('muscle', foreign_keys=[muscle_id_2], backref=db.backref('exercise_secondary', lazy=True))
    
    equipment = db.relationship('equipment', secondary=exercise_equipment, backref=db.backref('exercises', lazy='dynamic'))

    def __init__(self, exercise_api_id, name, description, category_id, muscle_id, muscle_id_2):
        self.exercise_api_id = exercise_api_id
        self.name = name
        self.description = description
        #self.cat_name = cat_name
        self.category_id = category_id
        self.muscle_id = muscle_id
        self.muscle_id_2 = muscle_id_2
        

    def __repr__(self):
        return ("exercise: {{self.name}}")