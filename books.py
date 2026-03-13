from fastapi import Body, FastAPI

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


@app.get("/books/byauthor/")
async def read_book_by_author(author: str):
    return_book_by_author = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            return_book_by_author.append(book)

    return return_book_by_author


@app.get("/books/{author_name}/")
async def read_author(author_name: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == author_name.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get("title").casefold():
            BOOKS[i] = updated_book


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break
