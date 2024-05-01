from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('Заказчик', 'Заказчик'),
        ('Исполнитель', 'Исполнитель'),
    )
    role = models.CharField(max_length=15, choices=ROLE_CHOICES)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
