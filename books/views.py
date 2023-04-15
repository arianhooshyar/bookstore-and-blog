from django.shortcuts import render
from .models import Book, Comment
from django.views import generic
from django.urls import reverse_lazy


class BookListView(generic.ListView):
    model = Book
    paginate_by = 2
    template_name = 'book/book_list_view.html'
    context_object_name = 'books'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    context_object_name = 'books'


class BookCreateView(generic.CreateView):
    model = Book
    fields = ['title', 'author', 'content', 'price', 'cover']
    template_name = 'book/book_create.html'


class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ['title', 'author', 'price']
    template_name = 'book/book_update.html'


class BookDeleteView(generic.DeleteView):
    model = Book
    fields = ['title', 'author', 'price']
    template_name = 'book/book_detete_view.html'
    success_url = reverse_lazy('Book_list_view')
    context_object_name = 'books'


