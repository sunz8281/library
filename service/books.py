from data import books as data

def add_book(title, author):
    try:
        data.add_book(title, author)
        return True
    except Exception as ex:
        print(ex)
        return False


def get_books():
    try:
        books = data.get_books()
        return [{'title': book[0], 'author': book[1]} for book in books]
    except Exception as ex:
        print(ex)
        return None


def delete_book(book_id):
    try:
        if data.get_book_available_by_id(book_id):
            data.delete_book(book_id)
            return True
        else:
            return False
    except Exception as ex:
        print(ex)
        return False

