from django.http import HttpResponseBadRequest

from functools import wraps


def ajax_required(func):
    """Фуккия-декоратор для проверки того,
    что запрос на обработчик откправлен с помощью ajax"""
    @wraps(func)
    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest
    return wrap
