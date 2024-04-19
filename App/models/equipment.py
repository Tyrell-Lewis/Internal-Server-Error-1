from App.database import db

class equipment(db.Model):
    equip_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)
    
    
    def __init__(self, equip_id, name):
        self.equip_id = equip_id
        self.name = name

    def __repr__(self):
        return f"Category(name={self.name})"