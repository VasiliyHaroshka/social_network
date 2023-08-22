from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Action(models.Model):
    """Модель описания активностей пользователя"""
    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        db_index=True,
        related_name="actions",
    )
    act = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True, db_index=True)
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="target_object",
    )
    object_id = models.PositiveIntegerField(null=True, blank=True, db_index=True)
    target = GenericForeignKey(
        "content_type",
        "object_id",
    )

    def __str__(self):
        return f"{self.user} did {self.act} at {self.time}."

    class Meta:
        ordering = ("-time",)
