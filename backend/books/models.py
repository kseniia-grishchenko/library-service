from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self) -> str:
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=63)
    authors = models.ManyToManyField(Author, blank=True)
    description = models.TextField()
    genres = models.ManyToManyField(Genre, blank=True)
    daily_annual_fee = models.DecimalField(
        "Daily annual fee", max_digits=7, decimal_places=2, default=0.02
    )

    def __str__(self) -> str:
        return self.title
