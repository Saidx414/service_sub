from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Tariff, UserSubscription
from .serializers import TariffSerializer, UserSubscriptionSerializer
from django.contrib.auth import get_user_model
from .sub_permissions import IsAdminOrAuthenticated
from rest_framework import status


class TariffViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tariff.objects.all()
    serializer_class = TariffSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly)


class UserSubscriptionViewSet(viewsets.ModelViewSet):
    # queryset = UserSubscription.objects.all()
    permission_classes = [IsAdminOrAuthenticated]
    serializer_class = UserSubscriptionSerializer

    def get_queryset(self):
        user = self.request.user
        if not user or not user.is_authenticated:
            return UserSubscription.objects.none()

        if user.is_staff:
            return UserSubscription.objects.all()
        return UserSubscription.objects.filter(user=user)

