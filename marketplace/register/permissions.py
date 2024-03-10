from django.http import Http404
from main_app.models import User as CustomUser


class ProfilePermissionsMixin:
    """provides functions to check if user is authorized to modify a record"""

    def has_permissions(self) -> bool:
        """checks if user is authenitcated and has permission to modify (moder/admin or creator)"""
        if not self.request.user.is_authenticated:
            return False
        user_django = CustomUser.objects.filter(user_django=self.request.user)
        return self.kwargs['pk'] == user_django[0].pk

    def dispatch(self, request, *args, **kwargs):
        """if user doesn't have permission raises error, otherwise - calls dispatch function from generic class"""
        if not self.has_permissions():
            group = self.request.user.groups.values('name')[0]['name']
            if group == 'admin':
                msg_for_admin = 'Зайдите в панель администратора для редактирования записей пользователей'
            else:
                msg_for_admin = ''
            raise Http404(f'Вы не можете заходить в профиль других пользователей.\n{msg_for_admin}')
        return super().dispatch(request, *args, **kwargs)


class PasswordPermissionsMixin:
    """provides functions to check if user is authorized to modify a record"""

    def has_permissions(self) -> bool:
        """checks if user is authenitcated and has permission to modify (moder/admin or creator)"""
        if not self.request.user.is_authenticated:
            return False
        return self.kwargs['pk'] == self.request.user.pk

    def dispatch(self, request, *args, **kwargs):
        """if user doesn't have permission raises error, otherwise - calls dispatch function from generic class"""
        if not self.has_permissions():
            group = self.request.user.groups.values('name')[0]['name']
            if group == 'admin':
                msg_for_admin = 'Зайдите в панель администратора для редактирования записей пользователей'
            else:
                msg_for_admin = ''
            raise Http404(f'Вы не можете заходить в профиль других пользователей.\n{msg_for_admin}')
        return super().dispatch(request, *args, **kwargs)
