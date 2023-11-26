from django.urls import path
from .views import GenreListAPIView, AuthorListAPIView, BookListAPIView, BookDetailAPIView, BookIsAvailable


app_name = "books"

urlpatterns = [
    path('genres/', GenreListAPIView.as_view(), name='genre-list'),
    path('authors/', AuthorListAPIView.as_view(), name='author-list'),
    path('', BookListAPIView.as_view(), name='book-list'),
    path('<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
    path('is_available/<int:pk>/', BookIsAvailable.as_view(), name='book-available')
]
