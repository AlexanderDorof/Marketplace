from django.core.paginator import Paginator
from django.db.models.query import QuerySet

from .models import User


class DataMixin:
    """Mixin that binds logged-in user with its custom model User. Add some consts to context based on group,
    user belong"""

    def get_user_context(self, **kwargs) -> dict:
        """for authenticated users adds to context consts: is_authenticated, is_moderator, is_admin, username,
        django_user_pk, django_user"""
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
    """mixin adds pagination to class-based view"""

    def paginated_object(self, queryset: QuerySet) -> QuerySet:
        """function excepts full queryset and return one page"""
        item_list = queryset
        paginator = Paginator(item_list, self.paginate_by)
        page = self.request.GET.get('page')
        return paginator.get_page(page)


def funcmixin(request, **kwargs) -> dict:
    """Function that binds logged-in user with its custom model User. Add some consts to context based on group,
    user belong"""
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
