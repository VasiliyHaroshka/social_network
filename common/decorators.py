from django.http import HttpResponseBadRequest

from functools import wraps


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def ajax_required(func):
    """Фуккия-декоратор для проверки того,
    что запрос на обработчик откправлен с помощью ajax"""

    @wraps(func)
    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest

    return wrap
