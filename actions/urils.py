from django.contrib.contenttypes.models import ContentType
from django.utils.timezone import now

from .models import Action

from datetime import timedelta


def create_action(user, act, target=None):
    """Создание активности пользователя и связывание её с объектом target (если он есть)"""
    last_minute = now() - timedelta(seconds=60)
    the_same_actions = Action.objects.filter(
        user_id=user.id,
        act=act,
        time__gte=last_minute,
    )
    if target:
        content_type = ContentType.objects.get_for_model(target)
        the_same_actions = the_same_actions.filter(
            content_type=content_type,
            object_id=target.id,
        )
    if not the_same_actions:
        action = Action(
            user,
            act=act,
            target=target,
        )
        action.save()
        return True
    return False

