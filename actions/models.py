from django.db import models


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

    def __str__(self):
        return f"{self.user} did {self.act} at {self.time}."

    class Meta:
        ordering = ("-time",)
