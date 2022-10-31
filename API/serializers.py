from rest_framework import serializers

from API.models import Book


class BookSearchSerializer(serializers.ModelSerializer):
    """Serializer for Book model to list data of search."""

    class Meta:
        model = Book
        fields = 'book_id', 'title', 'authors', 'languages', 'download_count'


class BookDetailSerializer(serializers.ModelSerializer):
    """Serializer for Book model to book details."""

    class Meta:
        model = Book
        fields = '__all__'


class BookReviewSerializer(serializers.ModelSerializer):
    """Serializer for Book model to book review."""

    class Meta:
        model = Book
        fields = ['book_id', 'rating', 'reviews']

    def validate_rating(self, value):
        if value < 0 or value > 5:
            raise serializers.ValidationError('The rating should be between 0 and 5')
        return value
