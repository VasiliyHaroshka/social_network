from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class EmailAuthentication:
    """Бэкэнд аутентификации по email"""

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except:
            return None
