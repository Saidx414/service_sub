from django.contrib.auth.models import AbstractUser
from django.db import models
from service import settings

class Tariff(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()


class UserSubscription(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='subscription',
    )
    tariff = models.ForeignKey(Tariff, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, unique=True, blank=True, default='')
    telegram_id = models.CharField(max_length=100, blank=True, default='')

