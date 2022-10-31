from rest_framework.response import Response
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView

from API.models import Book
from API.serializers import BookSearchSerializer, BookDetailSerializer, BookReviewSerializer


class BookSearch(generics.ListAPIView):
    """View to get Book Search Result."""

    serializer_class = BookSearchSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']

    def get_queryset(self):
        queryset = Book.objects.all()
        return queryset


class BookDetail(generics.ListAPIView):
    """View to get Book Detail."""

    serializer_class = BookDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['book_id']

    def get_queryset(self):
        queryset = Book.objects.all()
        return queryset


class BookReview(APIView):
    """
    Post review and rating of book.
    """

    def post(self, request):
        # Check if we have that book id on our DB
        id = request.data.get('book_id', None)
        if not Book.objects.filter(book_id=self.request.data['book_id']).exists():
            return Response({"error": "That book id does not exist."})
        book_update = Book.objects.get(book_id=id)
        serializer = BookReviewSerializer(book_update, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
