from fastapi import APIRouter, Body
from service import borrowers as service

router = APIRouter(prefix="/borrowers")

@router.get("/{borrower}/books")
def get_borrowing_books(borrower):
    return service.get_borrowing_books(borrower)

