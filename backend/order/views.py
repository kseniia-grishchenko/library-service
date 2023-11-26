# views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from payments.models import Payment
from payments.serializers import PaymentSerializer
from .models import Order
from .serializers import OrderSerializer
from borrowings.models import Borrowing
from django.utils import timezone
from datetime import timedelta


class PaymentCreateView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def create(self, request, *args, **kwargs):
        order_data = request.data.get('order')
        books_data = order_data.get('books', [])

        borrowings = []

        for book_data in books_data:
            book_id = book_data.get('book_id')

            borrowing = Borrowing.objects.create(
                book_id=book_id,
                user=request.user,
            )

            expected_return_date = timezone.now() + timedelta(days=Borrowing.BORROW_TERM)
            borrowing.expected_return_date = expected_return_date
            borrowing.save()

            borrowings.append(borrowing)

        response = super().create(request, *args, **kwargs)

        payment_id = response.data.get('id')

        for borrowing in borrowings:
            borrowing.payment_id = payment_id
            borrowing.save()

        return response


@api_view(['PUT'])
def change_order_status(request, order_id):
    order = Order.objects.get(pk=order_id)

    order.is_sent = not order.is_sent
    order.save()

    return Response({'status': 'Order status changed successfully'}, status=status.HTTP_200_OK)
