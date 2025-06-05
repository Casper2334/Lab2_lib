def get_book_model(db):
    class Book(db.Model):
        __tablename__ = 'books'
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(100), nullable=False)
        author = db.Column(db.String(100), nullable=False)
        year = db.Column(db.Integer, nullable=False)
        reader_id = db.Column(db.Integer, db.ForeignKey('reader.id'), nullable=True)

        def __repr__(self):
            return f'<Book {self.title}>'
    return Book
