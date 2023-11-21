from rest_framework import serializers

from borrowings.serializers import BorrowingRetrieveSerializer
from payments.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = (
            "id",
            "borrowing",
            "status",
            "type_status",
            "session_url",
            "session_id",
            "money_to_pay",
        )
        read_only_fields = (
            "id",
            "money_to_pay",
        )


class PaymentRetrieveSerializer(PaymentSerializer):
    borrowing = BorrowingRetrieveSerializer()
