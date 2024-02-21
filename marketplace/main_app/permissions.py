from django.http import Http404
from icecream import ic


class AuthorPermissionsMixin:
    def has_permissions(self):
        if not self.request.user.is_authenticated:
            return False
        seller = self.get_object().seller
        group = self.request.user.groups.values('name')[0]['name']
        return group in ('admin', 'moderator') or seller.user_django == self.request.user

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            if self.__class__.__name__.endswith('EditView'):
                action = 'Редактировать'
            elif self.__class__.__name__.endswith('DeleteView'):
                action = 'Удалять'
            else:
                action = ''
            raise Http404(f'{action} записи может только автор и модератор')
        return super().dispatch(request, *args, **kwargs)
