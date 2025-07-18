from django.contrib import admin
from .models import Tariff, UserSubscription, CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

admin.site.register(Tariff)
admin.site.register(UserSubscription)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['id', 'username', 'email', 'phone', 'telegram_id', 'is_active']

    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительная информация', {'fields': ('phone', 'telegram_id')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Дополнительная информация', {'fields': ('phone', 'telegram_id')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)



