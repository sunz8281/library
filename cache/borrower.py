import service
from . import redis_client

def test():
    return "redis connect ok"

def add_borrowing(borrower, title):
    key = f"borrower:{borrower}:books"
    redis_client.sadd(key, title)

def remove_borrowing(borrower, title):
    key = f"borrower:{borrower}:books"
    redis_client.srem(key, title)

def get_borrowing_books(borrower):
    key = f"borrower:{borrower}:books"
    return redis_client.smembers(key)