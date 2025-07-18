from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Order
from .serializers import OrderSerializer
from products.utils import notify_telegram
from django.contrib.auth import get_user_model


User = get_user_model()

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        user_id = self.request.headers.get('X-User-ID')
        if not user_id:
            raise ValueError("Не передан X-User-ID")

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise ValueError("Пользователь не найден")

        order = serializer.save(user=user)
        notify_telegram(user)


