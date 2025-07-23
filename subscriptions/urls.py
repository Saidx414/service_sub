from django.urls import path, include
from rest_framework import routers
from .views import TariffViewSet, UserSubscriptionViewSet


router = routers.DefaultRouter()
router.register(r'tariffs', TariffViewSet)
router.register(r'subscriptions', UserSubscriptionViewSet, basename='subscriptions')

urlpatterns = [
    path('', include(router.urls)),

]

