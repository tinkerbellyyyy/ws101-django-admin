from django.db import models

class Books(models.Model):
    book_id = models.CharField(max_length=255)
    book_name = models.CharField(max_length=255)
    book_author = models.CharField(max_length=255)
    date_publish = models.CharField(max_length=255)