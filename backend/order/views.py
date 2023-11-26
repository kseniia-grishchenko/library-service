from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.utils import timezone
from datetime import timedelta

from payments.models import Payment
from payments.serializers import PaymentSerializer
from .models import Order
from .serializers import OrderSerializer
from borrowings.models import Borrowing
import uuid


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        order_data = request.data.get('order')
        books_data = order_data.get('books', [])

        borrowings = []

        for book_data in books_data:
            book_id = book_data.get('book_id')
            borrowing = Borrowing.objects.create(
                book_id=book_id,
                user=request.user
            )

            expected_return_date = timezone.now() + timedelta(days=Borrowing.BORROW_TERM)
            borrowing.expected_return_date = expected_return_date
            borrowing.save()

            random_session_url = f"https://example.com/session/{uuid.uuid4()}"
            random_session_id = str(uuid.uuid4())

            payment_data = {
                'status': 'PENDING',
                'money_to_pay': borrowing.total_price,
                'user': request.user.id,
                'borrowing': borrowing.id,
                'session_url': random_session_url,
                'type_status': Payment.TypeChoices.PAYMENT,
                'session_id': random_session_id,
            }
            payment_serializer = PaymentSerializer(data=payment_data)
            payment_serializer.is_valid(raise_exception=True)
            payment = payment_serializer.save()

            borrowing.payment = payment
            borrowing.save()

            borrowings.append(borrowing)

        order_data['user'] = request.user.id
        order_data['borrowings'] = [borrowing.id for borrowing in borrowings]
        order_serializer = OrderSerializer(data=order_data)
        order_serializer.is_valid(raise_exception=True)
        order_serializer.save()

        return Response(order_serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def change_order_status(request, order_id):
    order = Order.objects.get(pk=order_id)
    order.is_sent = not order.is_sent
    order.save()

    return Response({'status': 'Order status changed successfully'}, status=status.HTTP_200_OK)
