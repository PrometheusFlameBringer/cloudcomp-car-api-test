from fastapi import FastAPI, HTTPException, Header, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Simple Book API",
    description="A beginner-friendly REST API containing information about books.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# BOOK DATA
books = [

    {
        "id": 1,
        "title": "The Count of Monte Cristo",
        "author": "Alexandre Dumas",
        "year": 1846,
        "genre": "Adventure",
        "rating": 4.34,
        "description": "A tale of revenge and redemption."
    },

    {
        "id": 2,
        "title": "The Three Musketeers",
        "author": "Alexandre Dumas",
        "year": 1844,
        "genre": "Adventure",
        "rating": 4.1,
        "description": "A tale of friendship and adventure in 17th-century France."
    },

    {
        "id": 3,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": 1925,
        "genre": "Fiction",
        "rating": 3.93,
        "description": "A classic American novel set in the Jazz Age."
    },

    {
        "id": 4,
        "title": "El filibusterismo",
        "author": "José Rizal",
        "year": 1891,
        "genre": "Fiction",
        "rating": 4.26,
        "description": "The continuation of the story of Noli Me Tangere, focusing on darker themes."
    },

    {
        "id": 5,
        "title": "Little Women",
        "author": "Louisa May Alcott",
        "year": 1868,
        "genre": "Fiction",
        "rating": 4.3,
        "description": "A coming-of-age story of four sisters detailing their passage from childhood to womanhood."
    }

]

# HOME
@app.get("/")
def home():

    return {
        "message": "Welcome to the Simple Book API!",
        "endpoints": [
            "/books",
            "/books/{id}",
            "/books/search"
        ]
    }


# GET ALL BOOKS
@app.get("/books")
def get_books():

    return {
        "count": len(books),
        "books": books
    }

# SEARCH BOOKS
@app.get("/books/search")
def search_books( q: str = Query(..., min_length=1)):
    q = q.lower()
    results = []
    for book in books:
        searchable_text = (
            f"{book['title']} "
            f"{book['author']} "
            f"{book['genre']}"
            f"{book['year']}"
        ).lower()

        if q in searchable_text:
            results.append(book)

    return {
        "query": q,
        "count": len(results),
        "results": results
    }

# GET ONE BOOK
@app.get("/books/{book_id}")
def get_book(book_id: int):

    for book in books:

        if book["id"] == book_id:
            return book

    raise HTTPException(
        status_code=404,
        detail="Book not found."
    )