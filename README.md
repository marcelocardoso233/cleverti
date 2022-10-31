# Cleverti Exercise

## Installation and Running

### Required Configuration

Run `pip install Django` and after that `python3 manage.py shell` and run the function with the commands below to populate the model, after that you can test the endpoints with the query parameters.

### Python Functions

`from API.utils import sync_books`

`sync_books()`

### Main Project

* `docker-compose build cleverti`
* `docker-compose up`

### ENDPOINTS

http://127.0.0.1:8000/api/book_search/

http://127.0.0.1:8000/api/book_search/?title=...

http://127.0.0.1:8000/api/book_detail/?book_id=...

http://127.0.0.1:8000/api/book_review

### EXAMPLE OF PAYLOAD TO REVIEW A BOOK


    {
        "book_id": 67979,
        "rating": 4,
        "reviews": "Test"
    }

