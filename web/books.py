from fastapi import APIRouter, Body
from service import books as service

router = APIRouter(prefix="/books")

@router.post("")
def add_book(book = Body()):
    return service.add_book(book['title'], book['author'])

@router.get("")
def get_books():
    return service.get_books()

@router.delete("/{book_id}")
def delete_book(book_id):
    return service.delete_book(book_id)