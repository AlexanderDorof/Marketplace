from icecream import ic


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        group_queryset = self.request.user.groups.values('name')
        group = group_queryset[0]['name']
        context['is_authenticated'] = self.request.user.is_authenticated
        context['is_moderator'] = group in ('moderator', 'admin')
        context['is_admin'] = group in ('admin',)
        context['username'] = self.request.user.username
        return context


def funcmixin(request, **kwargs):
    context = kwargs
    group_queryset = request.user.groups.values('name')
    group = group_queryset[0]['name']
    context['is_authenticated'] = request.user.is_authenticated
    context['is_moderator'] = group in ('moderator', 'admin')
    context['is_admin'] = group in ('admin',)
    context['username'] = request.user.username
    return context
