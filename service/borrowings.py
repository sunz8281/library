from data import borrowings as data
from data import books as books_data
from cache import borrower as cache

def test():
    db_test = data.test()
    redis_test = cache.test()
    return {"sqlite": db_test, "redis": redis_test}


def borrow(borrower, title):
    try:
        book = books_data.get_book_by_title(title)
        book_id = book[0]
        if book[1] == 1:
            books_data.update_book_available(book_id, 0)
            data.add_borrowings(borrower, book_id)
            cache.add_borrowing(borrower, title)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

def return_book(borrower, title):
    try:
        book = books_data.get_book_by_title(title)
        book_id = book[0]
        if book[1] == 0:
            books_data.update_book_available(book_id, 1)
            data.update_return(borrower, book_id)
            cache.remove_borrowing(borrower, title)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def get_borrowing_books_by_month(borrow_month):
    books = data.get_borrowing_books_by_month(borrow_month)
    return [{'borrower': book[0], 'title':book[1], 'author':book[2]} for book in books]