from . import views
from django.urls import path

urlpatterns = [
    path('books/', views.books, name='books'),
    path('books/<int:id>/', views.book_full_view, name='details'),
    path('book/<int:id>/update/', views.update_books, name='update'),
    path('book/<int:id>/delete/', views.delete_books, name='delete'),
    path('add-books/', views.books_create_id, name='create'),
]