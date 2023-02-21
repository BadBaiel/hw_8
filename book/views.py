from django.shortcuts import render, get_object_or_404
from . import models


def books(request):
    """
        Вывод неполной информации
    """
    books = models.Book.objects.all()
    return render(request, 'books.html', {'books': books})


def book_full_view(request, id):
    """
        Вывод полной информации по id
    """
    books_id = get_object_or_404(models.Book, id=id)
    return render(request, 'books_detail.html', {'books_id': books_id})


def book_delete(request):
    """
        Функция для удаления поста с приложения
    """
