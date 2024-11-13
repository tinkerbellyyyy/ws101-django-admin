from django.template import loader
from django.http import HttpResponse
from .models import Books
from .forms import BookForm
from django.shortcuts import render, redirect, get_object_or_404

def books(request):
    mybooks = Books.objects.all().values()
    template = loader.get_template('all_books.html')
    context = {
        'mybooks' : mybooks,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    # Fetch the specific book using the id
    mybook = get_object_or_404(Books, id=id)  # This fetches the specific book or returns a 404 if not found
    context = {
        'mybook': mybook,  # Pass the single book to the template
    }
    return render(request, 'details.html', context)  # Render the template with the specific book

def main(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        book_id = request.POST.get('book_id')  # Get the book ID from the form input

        if form.is_valid():
            # Optionally, you might want to set the book ID if you're allowing manual input
            # Make sure to handle any potential conflicts with existing IDs
            # For example, you could check if the ID already exists in the database
            form.save()  # Save the book to the database
            return redirect('books')  # Redirect to the book list after saving
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = BookForm()
    
    return render(request, 'add_book.html', {'form': form})

def edit_book(request, book_id):
    book = get_object_or_404(Books, id=book_id)  # Fetch the existing book

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)  # Bind the form with the book instance
        if form.is_valid():
            form.save()  # Save the updated book details
            return redirect('books')  # Redirect to the book list after saving
    else:
        form = BookForm(instance=book)  # Pre-fill the form with the current book's details

    return render(request, 'edit_book.html', {'form': form, 'book': book})

def delete_book(request, book_id):
    book = get_object_or_404(Books, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('books')  # Redirect to the book list after deletion
    return render(request, 'confirm_delete.html', {'book': book})