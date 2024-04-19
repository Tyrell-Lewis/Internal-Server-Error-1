from App.database import db

class muscle(db.Model):
    musc_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)
    name_en = db.Column(db.String(120), nullable=False, unique=True)
    
    def __init__(self, musc_id, name, name_en):
        self.musc_id = musc_id
        self.name = name
        self.name_en = name_en

    def __repr__(self):
        return f"Category(name={self.name})"