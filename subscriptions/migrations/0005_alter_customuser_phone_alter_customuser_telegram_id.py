# Generated by Django 4.2.3 on 2025-07-23 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0004_usersubscription_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='telegram_id',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
