from fastapi import APIRouter, Body
from service import borrowings as service

router = APIRouter(prefix="/borrows")

@router.post("")
def borrow(borrow_info=Body()):
    return service.borrow(borrow_info['borrower'], borrow_info['title'])

@router.get("/month/{borrow_month}")
def get_borrowing_book_by_month(borrow_month):
    return service.get_borrowing_books_by_month(borrow_month)

