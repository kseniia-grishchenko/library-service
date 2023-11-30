from rest_framework import serializers

from borrowings.serializers import BorrowingSerializer
from .models import Order


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class OrderListSerializer(serializers.ModelSerializer):
    borrowings = BorrowingSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'
