from dao.book_dao import BookDAO

class BookService:
    @staticmethod
    def get_all_books():
        return BookDAO.get_all_books()

    @staticmethod
    def get_book_by_id(book_id):
        return BookDAO.get_book_by_id(book_id)

    @staticmethod
    def create_book(title, author, year, reader_id):
        if not title or not author or not year:
            raise ValueError("Усі поля (назва, автор, рік) повинні бути заповнені")
        try:
            year = int(year)
            if year < 0:
                raise ValueError("Рік видання не може бути від’ємним")
            return BookDAO.create_book(title, author, year, reader_id)
        except ValueError as e:
            raise ValueError(str(e))
        except Exception as e:
            raise Exception(f"Помилка при створенні книги: {str(e)}")

    @staticmethod
    def update_book(book_id, title, author, year, reader_id):
        if not title or not author or not year:
            raise ValueError("Усі поля (назва, автор, рік) повинні бути заповнені")
        try:
            year = int(year)
            if year < 0:
                raise ValueError("Рік видання не може бути від’ємним")
            return BookDAO.update_book(book_id, title, author, year, reader_id)
        except ValueError as e:
            raise ValueError(str(e))
        except Exception as e:
            raise Exception(f"Помилка при оновленні книги: {str(e)}")

    @staticmethod
    def delete_book(book_id):
        return BookDAO.delete_book(book_id)