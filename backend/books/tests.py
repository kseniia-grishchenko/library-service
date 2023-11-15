from rest_framework.test import APIClient
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User

from .models import Genre, Book, Author
from .serializers import GenreSerializer, AuthorSerializer, BookSerializer

GENRE_URL = reverse("books:genre-list")
AUTHOR_URL = reverse("books:author-list")
BOOK_LIST_URL = reverse("books:book-list")
BOOK_DETAIL_URL = lambda book_id: reverse("books:book-detail", args=[book_id])


def sample_author(full_name="John Doe"):
    return Author.objects.create(full_name=full_name)


def sample_genre(name="Fantasy"):
    return Genre.objects.create(name=name)


def sample_book(title="Sample Book", **params):
    defaults = {
        "description": "little book",
        "daily_annual_fee": 1.00,
    }
    authors = params.pop('authors', [])
    genres = params.pop('genres', [])

    defaults.update(params)
    book = Book.objects.create(title=title, **defaults)

    if authors:
        book.authors.set(authors)
    if genres:
        book.genres.set(genres)

    return book




class PublicGenreApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_list_genres(self):
        Genre.objects.create(name="Fantasy")
        Genre.objects.create(name="Science Fiction")

        response = self.client.get(GENRE_URL)

        genres = Genre.objects.order_by('name')
        serializer = GenreSerializer(genres, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


class PublicAuthorApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_list_authors(self):
        Author.objects.create(full_name="John Doe")
        Author.objects.create(full_name="Jane Doe")

        response = self.client.get(AUTHOR_URL)

        authors = Author.objects.order_by('-full_name')
        serializer = AuthorSerializer(authors, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


class BookDetailApiTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@test.com",
            password="testpass"
        )
        self.user.is_staff = True
        self.user.save()

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_retrieve_book(self):
        author = sample_author()
        genre = sample_genre()
        book = sample_book(title="Sample Book", authors=[author], genres=[genre])
        url = BOOK_DETAIL_URL(book.id)

        response = self.client.get(url)

        serializer = BookSerializer(book)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


class PublicBookApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_retrieve_books(self):
        sample_book(title="Book1")
        sample_book(title="Book2")

        response = self.client.get(BOOK_LIST_URL)

        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_filter_books_by_genre(self):
        genre1 = sample_genre(name="Fantasy")
        genre2 = sample_genre(name="Science Fiction")
        book1 = sample_book(title="Fantasy Book", genres=[genre1])
        sample_book(title="Other Book", genres=[genre2])

        response = self.client.get(BOOK_LIST_URL, {'genre': 'Fantasy'})

        serializer = BookSerializer([book1], many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_filter_books_by_author(self):
        author1 = sample_author(full_name="John Doe")
        author2 = sample_author(full_name="Jane Doe")
        book1 = sample_book(title="Book by John", authors=[author1])
        sample_book(title="Book by Jane", authors=[author2])

        response = self.client.get(BOOK_LIST_URL, {'author': 'John'})

        serializer = BookSerializer([book1], many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
