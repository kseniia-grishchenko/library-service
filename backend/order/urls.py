from django.urls import path
from .views import PaymentCreateView, change_order_status


urlpatterns = [
    path('create_payment/', PaymentCreateView.as_view(), name='create-payment'),
    path('change_order_status/<int:order_id>/', change_order_status, name='change-order-status'),
]
