from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import TariffViewSet, UserSubscriptionViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = SimpleRouter()
router.register(r'tariffs', TariffViewSet)
router.register(r'subscriptions', UserSubscriptionViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),

]

