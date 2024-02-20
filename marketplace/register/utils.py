from icecream import ic
from main_app.models import User


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        if self.request.user.is_authenticated:
            group_queryset = self.request.user.groups.values('name')
            pk = self.request.user.pk
            user = User.objects.get(user_django__pk=pk)
            group = group_queryset[0]['name']
            context['is_authenticated'] = self.request.user.is_authenticated
            context['is_moderator'] = group in ('moderator', 'admin')
            context['is_admin'] = group in ('admin',)
            context['username'] = self.request.user.username
            context['django_user_pk'] = user.pk
        return context