from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.forms import ModelForm


from bookstore.models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

def index(request):
    books=Book.objects.all()
    return render(request,'bookstore/index.html',{
        'books': books,
    })

def book_detail(request,id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        raise Http404('This Book is not found')
    return render(request, 'bookstore/book_detail.html', {
        'book': book,
    })

def book_add(request):
    if request.POST:
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookstore')
    else:
        form = BookForm()
    return render(request, 'bookstore/addbook.html', {'form': form})


def book_edit(request,id):
    book = get_object_or_404(Book, id=id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('bookstore')
    return render(request, 'bookstore/addbook.html', {'form': form})

def book_delete(request,id):
    book=get_object_or_404(Book, id=id)
    book.delete()
    return redirect('bookstore')




