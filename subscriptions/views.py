from django.shortcuts import render
from rest_framework import viewsets
from .models import Tariff, UserSubscription
from .serializers import TariffSerializer, UserSubscriptionSerializer
from django.contrib.auth import get_user_model


User = get_user_model()

class TariffViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tariff.objects.all()
    serializer_class = TariffSerializer

class UserSubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = UserSubscriptionSerializer
    queryset = UserSubscription.objects.all()

    def get_queryset(self):
        user_id = self.request.headers.get("X-User-ID")
        if not user_id:
            return UserSubscription.objects.none()
        return UserSubscription.objects.filter(user_id=user_id)

    def perform_create(self, serializer):
        user_id = self.request.headers.get("X-User-ID")
        user = User.objects.get(id=user_id)
        serializer.save(user=user)

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

