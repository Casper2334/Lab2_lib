from database import db, Book

class BookDAO:
    @staticmethod
    def get_all_books():
        return Book.query.all()

    @staticmethod
    def get_book_by_id(book_id):
        return Book.query.get(book_id)

    @staticmethod
    def create_book(title, author, year, reader_id):
        book = Book(title=title, author=author, year=year, reader_id=reader_id)
        db.session.add(book)
        db.session.commit()
        return book

    @staticmethod
    def update_book(book_id, title, author, year, reader_id):
        book = Book.query.get(book_id)
        if book:
            book.title = title
            book.author = author
            book.year = year
            book.reader_id = reader_id
            db.session.commit()
        return book

    @staticmethod
    def delete_book(book_id):
        book = Book.query.get(book_id)
        if book:
            db.session.delete(book)
            db.session.commit()