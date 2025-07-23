from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Order
from .serializers import OrderSerializer
from products.utils import notify_telegram


class OrderViewSet(viewsets.ModelViewSet):
    # queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user
        if not user or not user.is_authenticated:
            return Order.objects.none()
        if user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(user=user)


    def perform_create(self, serializer):
        user = self.request.user

        if not user or not user.is_authenticated:
            raise ValueError("Пользователь не авторизован")

        order = serializer.save(user=user)
        notify_telegram(user)




