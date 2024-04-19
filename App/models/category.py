from App.database import db

class category(db.Model):
    cat_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)
    
    
    def __init__(self, cat_id, name):
        self.cat_id = cat_id
        self.name = name

    def __repr__(self):
        return f"Category(name={self.name})"