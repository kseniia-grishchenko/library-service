from rest_framework import serializers

from books.serializers import BookSerializer
from borrowings.serializers import BorrowingSerializer
from payments.models import Payment
from .models import Order


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
