from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = 'ADMIN', 'Администратор'
        USER = 'USER', 'Пользователь'
        CLIENT = 'CLIENT', 'Клиент'

    email = models.EmailField(
        unique=True,
        verbose_name="Email"
    )

    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.CLIENT,
        verbose_name="Роль"
    )

    bio = models.TextField(
        blank=True,
        verbose_name="Описание профиля"
    )

    birth_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Дата рождения"
    )

    is_verified = models.BooleanField(
        default=False,
        verbose_name="Подтвержден"
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email