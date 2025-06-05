from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    reader_id = db.Column(db.Integer, db.ForeignKey('reader.id'), nullable=True)

    def __repr__(self):
        return f'<Book {self.title}>'

class Reader(db.Model):
    __tablename__ = 'reader'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    books = db.relationship('Book', backref='reader', lazy=True)

    def __repr__(self):
        return f'<Reader {self.name}>'

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()