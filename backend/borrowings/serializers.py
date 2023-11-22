from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from books.serializers import BookSerializer
from borrowings.models import Borrowing
from payments.models import Payment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "password",
            "is_staff",
        )
        read_only_fields = ("is_staff",)
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}


class BorrowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowing
        fields = (
            "id",
            "borrow_date",
            "expected_return_date",
            "actual_return_date",
            "user",
            "book",
            "is_active",
        )


class BorrowingListSerializer(BorrowingSerializer):
    title = serializers.CharField(source="book.title", read_only=True)
    borrower = serializers.CharField(source="user.email", read_only=True)

    class Meta:
        model = Borrowing
        fields = (
            "id",
            "borrow_date",
            "expected_return_date",
            "actual_return_date",
            "title",
            "borrower",
        )


class BorrowingRetrieveSerializer(BorrowingSerializer):
    book = BookSerializer(many=False, read_only=True)
    user = UserSerializer(many=False, read_only=True)


class BorrowingCreateSerializer(BorrowingSerializer):
    class Meta:
        model = Borrowing
        fields = ("book",)

    def create(self, validated_data):
        book = validated_data["book"]
        user = validated_data["user"]

        if not book.is_available:
            raise ValidationError(f"Book '{book.title}' is out of stock")

        with transaction.atomic():
            borrowing = Borrowing.objects.create(book=book, user=user)
            Payment.objects.create(
                status="PENDING",
                money_to_pay=borrowing.book.daily_fee,
                borrowing=borrowing,
                user=borrowing.user_id,
            )
            book.save()

        return borrowing


class ReadBorrowSerializer(BorrowingSerializer):
    book = BookSerializer()
