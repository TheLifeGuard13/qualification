from django.contrib.auth.models import AbstractUser
from django.db import models

from config.settings import NULLABLE


class User(AbstractUser):
    """
    Модель Пользователя
    """

    username = None
    email = models.EmailField(unique=True, verbose_name="Почта")
    phone = models.CharField(max_length=35, **NULLABLE, verbose_name="Телефон")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: list = []
