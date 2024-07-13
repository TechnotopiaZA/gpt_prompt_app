from app import db

class Prompt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(100), nullable=False)
    needs = db.Column(db.String(200), nullable=False)
    task = db.Column(db.String(200), nullable=False)
    details = db.Column(db.Text, nullable=False)
    format = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Prompt {self.id} - {self.role}>'
