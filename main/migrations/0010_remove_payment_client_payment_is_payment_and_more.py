# Generated by Django 4.2.3 on 2023-09-02 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0009_lesson_is_public_lesson_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='client',
        ),
        migrations.AddField(
            model_name='payment',
            name='is_payment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='payment',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
