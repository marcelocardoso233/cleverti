from API.models import Book
import requests


def sync_books():
    """Fetch data from gutendex url and save it on model."""

    url = "https://gutendex.com/books/"
    headers = {'content-type': 'application/json'}
    response = requests.get(url=url, headers=headers)
    response_json = response.json()
    for book in response_json["results"]:
        queryset = Book.objects.filter(book_id=book["id"])
        if queryset.exists():
            db_instance = queryset.first()
        else:
            db_instance = Book()

        db_instance.book_id = book.get("id")
        db_instance.title = book.get("title")
        db_instance.authors = book.get("authors")
        db_instance.languages = book.get("languages")
        db_instance.download_count = book.get("download_count")
        db_instance.save()
