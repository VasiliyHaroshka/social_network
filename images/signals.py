from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from .models import Image


@receiver(m2m_changed, sender=Image.like.through)
def user_like_change(sender, instance, **kwargs):
    """Сигнал изменения количества лайков на картинке"""
    instance.count_likes = instance.like.count()
    instance.save()
