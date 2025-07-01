from cache import borrower as data


def get_borrowing_books(borrower):
    books = data.get_borrowing_books(borrower)
    book_list = [book.decode('utf-8') for book in books]
    return {'borrower':borrower, 'books':book_list }