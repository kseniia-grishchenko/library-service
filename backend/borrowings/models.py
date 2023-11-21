from django.conf import settings
from django.db import models
from django.db.models import Q, F

from books.models import Book
from .utils import calculate_expected_return_date


class Borrowing(models.Model):
    BORROW_TERM = 21
    EXPIRED_DATA_PRICE_FACTOR = 1.1

    borrow_date = models.DateField(auto_now_add=True)
    expected_return_date = models.DateField(
        null=True,
        default=calculate_expected_return_date(borrow_days=BORROW_TERM),
    )
    actual_return_date = models.DateField(null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="borrowings")
    is_active = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(expected_return_date__gt=F("borrow_date")),
                name="check_expected_return_date",
            ),
            models.CheckConstraint(
                check=Q(
                    Q(actual_return_date__isnull=True)
                    | Q(actual_return_date__gte=F("borrow_date")),
                ),
                name="check_actual_return_date",
            ),
        ]

    @property
    def total_price(self):
        return (
            self.book.daily_annual_fee
            * (self.expected_return_date - self.borrow_date).days
        )

    @property
    def fine_price(self):
        return (
                self.book.daily_annual_fee or self.BORROW_TERM
                * (self.actual_return_date - self.expected_return_date).days
        ) if self.actual_return_date else None

    def __str__(self) -> str:
        return f"{self.book}: {self.borrow_date} - {self.expected_return_date}."
