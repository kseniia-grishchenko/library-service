from django.db import models

from borrowings.models import Borrowing


class Order(models.Model):
    username = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    is_sent = models.BooleanField(default=False)
    borrowings = models.ManyToManyField(Borrowing)

    def __str__(self) -> str:
        return f"{self.username} {self.phone}"
