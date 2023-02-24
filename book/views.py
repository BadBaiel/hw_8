from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.http import HttpResponse


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


def delete_books(request, id):
    show_object = get_object_or_404(models.Book, id=id)
    show_object.delete()
    return HttpResponse('<h2>Книга успешна удалена</h2>')


def books_create_id(request):
    """
        Функция для добавления фильма через формы
    """
    method = request.method
    if method == "POST":
        form = forms.BooksForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h2>Список книг успешно обновлен!</h2>')

    else:
        form = forms.BooksForm()

    return render(request, 'add_books.html', {'form': form})


def update_books(request, id):
    books_object = get_object_or_404(models.Book, id=id)
    if request.method == 'POST':
        form = forms.BooksForm(instance=books_object, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h2>Книга успешна обновлена</h2>')
    else:
        form = forms.BooksForm(instance=books_object)

    return render(request, 'update_books.html', {
                                                    'form': form,
                                                    'object': books_object
                                                   })