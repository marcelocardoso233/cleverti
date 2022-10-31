from django.db import models


class Book(models.Model):
    """Book Model."""

    book_id = models.IntegerField(unique=True, null=True, blank=True)
    title = models.CharField(null=True, blank=True, max_length=320)
    authors = models.JSONField(blank=True, null=True)
    languages = models.JSONField(null=True)
    download_count = models.IntegerField(null=True)
    rating = models.FloatField(null=True, blank=True)
    reviews = models.JSONField(blank=True, null=True)

