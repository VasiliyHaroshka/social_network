from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Profile(models.Model):
    """Расширение стандартной модели пользователя"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    birth_date = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True)

    def __str__(self):
        return f"User's profile {self.user.username}"


class Contact(models.Model):
    """Связующая таблица для подписки пользователей друг на друга"""
    subscribed_from_user = models.ForeignKey(
        "auth.User",
        related_name="rel_from_set",
        on_delete=models.CASCADE,
    )
    subscribed_to_user = models.ForeignKey(
        "auth.User",
        related_name="rel_to_set",
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"{self.subscribed_from_user} follows {self.subscribed_to_user}"

    class Meta:
        ordering = ("-created",)


User.add_to_class('following',
                  models.ManyToManyField(
                      'self',
                      through=Contact,
                      related_name='followers',
                      symmetrical=False
                  )
                )
