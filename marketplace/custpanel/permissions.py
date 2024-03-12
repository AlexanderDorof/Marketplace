from django.http import Http404


class AdminPermissionsMixin:
    """provides functions to check if user is authorized to modify a record"""
    def has_permissions(self) -> bool:
        """checks if user is admin"""
        if not self.request.user.is_authenticated:
            return False
        group = self.request.user.groups.values('name')[0]['name']
        return group == 'admin'

    def dispatch(self, request, *args, **kwargs):
        """if user doesn't belong to admin group - raises error, otherwise - calls dispatch function from generic
        class"""
        if not self.has_permissions():
            raise Http404('У вас нет статуса админа для вхождения в админ-панель')
        return super().dispatch(request, *args, **kwargs)

def user_is_admin(user):
    if not user.is_authenticated:
        return False
    group = user.groups.values('name')[0]['name']
    return group == 'admin'