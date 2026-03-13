from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"title": "title One", "author": "author one", "category": "Science"},
    {"title": "title Two", "author": "author two", "category": "math"},
    {"title": "title Three", "author": "author three", "category": "Science"},
    {"title": "title Four", "author": "author four", "category": "history"},
    {"title": "title Five", "author": "author five", "category": "Science"},
    {"title": "title Six", "author": "author six", "category": "chemistry"},
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{book.title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book


@app.get("/books/")
async def books_category(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return


@app.get("/books/{author_name}/")
async def read_author(author_name: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == author_name.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return
