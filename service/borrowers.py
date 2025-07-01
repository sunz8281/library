from cache import borrower as data


def get_borrowing_books(borrower):
    books = data.get_borrowing_books(borrower)
    return {'borrower':borrower, books:[book for book in books] }