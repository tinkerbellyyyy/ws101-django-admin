from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('books/', views.books, name='books'),
    path('books/details/<int:id>/', views.details, name='details'),
    path('books/add/', views.add_book, name='add_book'),  # This should match your form action
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
]