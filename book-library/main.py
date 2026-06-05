from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

#stored in the dictionary
class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int

#received in Post and Put endpoints
class BookCreate(BaseModel):
    title: str
    author: str
    year: int

books = {}
next_id = 1

@app.post("/books/")
def create_book(new_book: BookCreate):
    global next_id

    book = Book(
        id = next_id,
        title = new_book.title,
        author = new_book.author,
        year = new_book.year
    )
    books[next_id] = book
    next_id += 1
    return book

@app.get("/books/")
def retrieve_all_books():
    if len(books) == 0:
        raise HTTPException(status_code=404, detail="there are no books")
    return list(books.values())

@app.get("/books/{id}")
def retrieve_this_book(id: int):
    if id not in books:
        raise HTTPException(status_code=404, detail="this book is not here")
    book = books[id]
    return book

@app.put("/books/{id}")
def update_book(id:int, new_book: BookCreate):
    if id not in books:
        raise HTTPException(status_code=404, detail="this book is not here")
    book = Book(
        id = id,
        title = new_book.title,
        author = new_book.author,
        year = new_book.year
    )
    books[id] = book
    return book

@app.delete("/books/{id}")
def delete_book(id: int):
    if id not in books:
        raise HTTPException(status_code=404, detail="this book is not here")
    del books[id]