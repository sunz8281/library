from . import con, cur

def test():
    return "sqlite connect ok"


def add_borrowings(borrower, book_id):
    sql = "insert into borrowings(book_id, borrower) values(?,?)"
    cur.execute(sql, (book_id, borrower))
    con.commit()


def get_borrowing_books_by_month(borrow_month):
    borrow_month = f"{int(borrow_month):02d}"
    print(borrow_month)
    sql = "select borrower, title, author from borrowings natural join books where strftime('%m', borrowed_at)=?"
    cur.execute(sql, (borrow_month, ))
    return cur.fetchall()