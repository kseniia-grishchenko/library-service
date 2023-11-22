from django.test import TestCase
from .models import Borrowing, Book
from django.contrib.auth.models import User
from datetime import date, timedelta
from django.db.utils import IntegrityError

class BorrowingModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.book = Book.objects.create(title='Test Book', daily_annual_fee=1.00)
        self.borrow_date = date.today()
        self.expected_return_date = self.borrow_date + timedelta(days=10)

    def test_total_price_calculation(self):
        borrowing = Borrowing.objects.create(
            book=self.book,
            user=self.user,
            expected_return_date=self.expected_return_date
        )
        expected_total_price = 10
        self.assertEqual(borrowing.total_price, expected_total_price)

    def test_fine_price_when_returned_late(self):
        actual_return_date = self.expected_return_date + timedelta(days=5)
        borrowing = Borrowing.objects.create(
            book=self.book,
            user=self.user,
            expected_return_date=self.expected_return_date,
            actual_return_date=actual_return_date
        )
        expected_fine = 5  # 5 days late * 1.00 fee per day
        self.assertEqual(borrowing.fine_price, expected_fine)

    def test_fine_price_when_returned_on_time(self):
        borrowing = Borrowing.objects.create(
            book=self.book,
            user=self.user,
            expected_return_date=self.expected_return_date,
            actual_return_date=self.expected_return_date
        )
        self.assertEqual(borrowing.fine_price, 0)

    def test_fine_price_when_not_yet_returned(self):
        borrowing = Borrowing.objects.create(
            book=self.book,
            user=self.user,
            expected_return_date=self.expected_return_date
        )
        self.assertIsNone(borrowing.fine_price)

    def test_constraint_on_expected_return_date(self):
        with self.assertRaises(IntegrityError):
            Borrowing.objects.create(
                book=self.book,
                user=self.user,
                expected_return_date=self.borrow_date - timedelta(days=1)
            )

    def test_constraint_on_actual_return_date(self):
        with self.assertRaises(IntegrityError):
            Borrowing.objects.create(
                book=self.book,
                user=self.user,
                expected_return_date=self.expected_return_date,
                actual_return_date=self.borrow_date - timedelta(days=1)
            )

