from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.managers import UserManager


class UserRoles(models.TextChoices):
    # TODO закончите enum-класс для пользователя 🟢
    ADMIN = "admin"
    USER = "user"


class User(AbstractUser):
    # TODO переопределение пользователя.🟢
    # TODO подробности также можно поискать в рекоммендациях к проекту🟢
    objects = UserManager()
    role = models.CharField(max_length=5, choices=UserRoles.choices, default=UserRoles.USER)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=30)
    image = models.ImageField(upload_to='logos/user/', null=True)
    username = models.CharField(_('username'), max_length=150, blank=True, null=True, )
    email = models.EmailField(_("email address"), unique=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
