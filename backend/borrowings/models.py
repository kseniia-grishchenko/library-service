from django.conf import settings
from django.db import models
from django.db.models import Q, F
from books.models import Book
from datetime import datetime, timedelta, date


class Borrowing(models.Model):
    BORROW_TERM = 21
    EXPIRED_DATA_PRICE_FACTOR = 1.01

    borrow_date = models.DateField(auto_now_add=True)
    expected_return_date = models.DateField(
        null=True,
        default=date.today() + timedelta(days=BORROW_TERM),
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
        expected_return_date = datetime.combine(self.expected_return_date, datetime.min.time()).date()
        borrow_date = datetime.combine(self.borrow_date, datetime.min.time()).date()

        return (
                self.book.daily_annual_fee
                * (expected_return_date - borrow_date).days
        )

    @property
    def fine_price(self):
        if self.actual_return_date:
            # Ensure both dates are datetime.date objects
            actual_return_date = datetime.combine(self.actual_return_date, datetime.min.time()).date()
            expected_return_date = datetime.combine(self.expected_return_date, datetime.min.time()).date()

            return (
                    self.book.daily_annual_fee or self.BORROW_TERM
                    * (actual_return_date - expected_return_date).days
            )
        return None

    def __str__(self) -> str:
        return f"{self.book}: {self.borrow_date} - {self.expected_return_date}."
