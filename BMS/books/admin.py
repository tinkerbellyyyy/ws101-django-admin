from django.contrib import admin
from .models import Books

class BooksAdmin(admin.ModelAdmin):
    list_display = ('book_id', 'book_name', 'book_author', 'date_publish')

admin.site.register(Books, BooksAdmin)
# Register your models here.
