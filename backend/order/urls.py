from django.urls import path
from .views import OrderCreateView, change_order_status


urlpatterns = [
    path('create_order/', OrderCreateView.as_view(), name='create-payment'),
    path('change_order_status/<int:order_id>/', change_order_status, name='change-order-status'),
]
