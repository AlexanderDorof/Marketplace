from django.http import Http404


class AuthorPermissionsMixin:
    """provides functions to check if user is authorized to modify a record"""

    def has_permissions(self) -> bool:
        """checks if user is authenitcated and has permission to modify (moder/admin or creator)"""
        if not self.request.user.is_authenticated:
            return False
        seller = self.get_object().seller
        group = self.request.user.groups.values('name')[0]['name']
        return group in ('admin', 'moderator') or seller.user_django == self.request.user

    def dispatch(self, request, *args, **kwargs):
        """if user doesn't have permission raises error, otherwise - calls dispatch function from generic class"""
        if not self.has_permissions():
            if self.__class__.__name__.endswith('EditView'):
                action = 'Редактировать'
            elif self.__class__.__name__.endswith('DeleteView'):
                action = 'Удалять'
            else:
                action = ''
            raise Http404(f'{action} записи может только автор и модератор')
        return super().dispatch(request, *args, **kwargs)
