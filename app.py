from flask import Flask, render_template, request, redirect, url_for, flash
from database import init_db, db
from services.book_service import BookService
from services.reader_service import ReaderService

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123321123@localhost:5432/library'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'supersecretkey'

init_db(app)

@app.route('/')
def index():
    books = BookService.get_all_books()
    return render_template('books_list.html', books=books)

@app.route('/book/new', methods=['GET', 'POST'])
def new_book():
    readers = ReaderService.get_all_readers()
    if request.method == 'POST':
        try:
            title = request.form['title']
            author = request.form['author']
            year = request.form['year']
            reader_id = request.form.get('reader_id')
            reader_id = int(reader_id) if reader_id else None
            BookService.create_book(title, author, year, reader_id)
            flash('Книгу успішно додано!', 'success')
            if reader_id is None:
                flash('Книга додана без читача.', 'info')
            return redirect(url_for('index'))
        except ValueError as e:
            flash(str(e), 'error')
        except Exception as e:
            flash('Помилка в опрацюванні запиту', 'error')
            db.session.rollback()
    return render_template('book_form.html', readers=readers, book=None)

@app.route('/book/<int:book_id>/edit', methods=['GET', 'POST'])
def edit_book(book_id):
    book = BookService.get_book_by_id(book_id)
    readers = ReaderService.get_all_readers()
    if request.method == 'POST':
        try:
            title = request.form['title']
            author = request.form['author']
            year = request.form['year']
            reader_id = request.form.get('reader_id')
            reader_id = int(reader_id) if reader_id else None
            BookService.update_book(book_id, title, author, year, reader_id)
            flash('Книгу успішно оновлено!', 'success')
            if reader_id is None:
                flash('Книга більше не видана читачу.', 'info')
            return redirect(url_for('index'))
        except ValueError as e:
            flash(str(e), 'error')
        except Exception as e:
            flash('Помилка в опрацюванні запиту', 'error')
            db.session.rollback()
    return render_template('book_form.html', readers=readers, book=book)

@app.route('/book/<int:book_id>/delete', methods=['POST'])
def delete_book(book_id):
    try:
        BookService.delete_book(book_id)
        flash('Книгу успішно видалено!', 'success')
    except Exception as e:
        flash('Помилка в опрацюванні запиту', 'error')
        db.session.rollback()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)