from django.urls import path
from . import views

urlpatterns = [

    path("book_search/", views.BookSearch.as_view()),
    path("book_detail/", views.BookDetail.as_view()),
    path("book_review/", views.BookReview.as_view()),
]
