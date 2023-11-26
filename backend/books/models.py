from django.db import models


def book_directory_path(instance, filename):
    return f'books/{instance.title}.{filename.split(".")[-1]}'


class Genre(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self) -> str:
        return self.name


class Author(models.Model):
    full_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.full_name


class Book(models.Model):
    title = models.CharField(max_length=63)
    authors = models.ManyToManyField(Author, blank=True)
    description = models.TextField()
    genres = models.ManyToManyField(Genre, blank=True)
    daily_annual_fee = models.DecimalField(
        "Daily annual fee", max_digits=7, decimal_places=2, default=0.01
    )
    image = models.ImageField(upload_to=book_directory_path, blank=True, null=True)

    def __str__(self) -> str:
        return self.title

    @property
    def is_available(self):
        return self.check_availability()

    def check_availability(self):
        from borrowings.models import Borrowing
        return Borrowing.objects.filter(book_id=self.id, is_actie=True).count() > 0
