from rest_framework import serializers
from .models import Genre, Author, Book


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', )


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('full_name', )


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    genres = GenreSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'
