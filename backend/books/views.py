from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Genre, Author, Book
from .serializers import GenreSerializer, AuthorSerializer, BookSerializer
from django.db.models import Q
from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404


class GenreListAPIView(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class AuthorListAPIView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListAPIView(ListCreateAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()

        authors = self.request.query_params.get('author')
        genres = self.request.query_params.get('genre')

        if authors:
            author_list = authors.split(',')
            author_query = Q()
            for author in author_list:
                author_query |= Q(authors__full_name__icontains=author)
            queryset = queryset.filter(author_query)

        if genres:
            genre_list = genres.split(',')
            genre_query = Q()
            for genre in genre_list:
                genre_query |= Q(genres__name__icontains=genre)
            queryset = queryset.filter(genre_query)

        return queryset


class BookDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookIsAvailable(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return JsonResponse({'is_available': book.is_available})
