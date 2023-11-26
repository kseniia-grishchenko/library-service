from django.db import models


class Order(models.Model):
    username = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)

    def __str__(self) -> str:
        return f"{self.username} {self.phone}"
