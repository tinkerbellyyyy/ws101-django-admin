# forms.py
from django import forms
from .models import Books

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['book_id', 'book_name', 'book_author', 'date_publish']  # Include book_id
        labels = {
            'book_id': 'Book ID:',
            'book_name': 'Book Name:',  # Custom label for book name
            'book_author': 'Book Author:',  # Custom label for book author
            'date_publish': 'Date Publish:',  # Custom label for date publish
        }