from django.db import models
from user.models import *

#Решил сделать одно приложение, без двух кабинетов, чтобы не повторяться.
class Customer(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(max_length=50)
    exp = models.TextField(max_length=650)

    def __str__(self):
        return self.user.username