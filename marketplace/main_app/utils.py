from django.core.paginator import Paginator
from icecream import ic

from .models import User


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        if self.request.user.is_authenticated:
            group_queryset = self.request.user.groups.values('name')
            group = group_queryset[0]['name']
            context['is_authenticated'] = self.request.user.is_authenticated
            context['is_moderator'] = group in ('moderator', 'admin')
            context['is_admin'] = group in ('admin',)
            context['username'] = self.request.user.username
            pk = self.request.user.pk
            user = User.objects.get(user_django__pk=pk)
            context['django_user_pk'] = user.pk
            context['django_user'] = user
        return context

class PaginationMixin:
    def paginated_object(self, obj, queryset=None):
        if not queryset:
            item_list = obj.objects.all().order_by('id')
        else:
            item_list = queryset
        paginator = Paginator(item_list, self.paginate_by)
        page = self.request.GET.get('page')
        return paginator.get_page(page)

def funcmixin(request, **kwargs):
    context = kwargs
    if request.user.is_authenticated:
        group_queryset = request.user.groups.values('name')
        group = group_queryset[0]['name']
        context['is_authenticated'] = request.user.is_authenticated
        context['is_moderator'] = group in ('moderator', 'admin')
        context['is_admin'] = group in ('admin',)
        context['username'] = request.user.username
        pk = request.user.pk
        user = User.objects.get(user_django__pk=pk)
        context['django_user_pk'] = user.pk
    return context
