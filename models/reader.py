from database import db  # Імпортуємо db із database.py

class Reader(db.Model):
    __tablename__ = 'reader'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    books = db.relationship('Book', backref='reader', lazy=True)

    def __repr__(self):
        return f'<Reader {self.name}>'