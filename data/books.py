from . import con, cur

def add_book(title, author):
    sql = "insert into books(title, author) values(?, ?)"
    cur.execute(sql, (title, author))
    con.commit()

def get_books():
    sql = "select title, author from books where available=1"
    cur.execute(sql)
    books = cur.fetchall()
    return books

def get_book_available_by_id(book_id):
    sql = "select count(*) from books where book_id = ? and available = 1"
    cur.execute(sql, (book_id,))
    is_available = cur.fetchone()[0]
    return is_available

def get_book_by_title(title):
    sql = "select book_id, available from books where title = ?"
    cur.execute(sql, (title,))
    book = cur.fetchone()
    return book

def delete_book(book_id):
    sql = "delete from books where book_id = ? and available = 1"
    cur.execute(sql, (book_id,))
    con.commit()

def update_book_available(book_id, available):
    sql = "update books set available = ? where book_id = ?"
    cur.execute(sql, (available, book_id))
    con.commit()