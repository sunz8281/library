from fastapi import APIRouter, Body
from service import borrowings as service

router = APIRouter(prefix="/return")

@router.post("")
def borrow(borrow_info=Body()):
    return service.return_book(borrow_info['borrower'], borrow_info['title'])