from django.http import Http404


class AdminPermissionsMixin:
    """provides functions to check whether user is admin"""

    def has_permissions(self) -> bool:
        """checks if user is admin"""
        if not self.request.user.is_authenticated:
            return False
        group = self.request.user.groups.values("name")[0]["name"]
        return group == "admin"

    def dispatch(self, request, *args, **kwargs):
        """if user doesn't belong to admin group - raises error, otherwise - calls dispatch function from generic
        class"""
        if not self.has_permissions():
            raise Http404(
                "У вас нет статуса администратора для вхождения в админ-панель"
            )
        return super().dispatch(request, *args, **kwargs)


def user_is_admin(user) -> str:
    """Function is used in permission decorator to check whether user is admin. For views based on functions"""
    if not user.is_authenticated:
        return False
    group = user.groups.values("name")[0]["name"]
    return group == "admin"
