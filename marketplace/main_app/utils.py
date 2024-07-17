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
            group_queryset = self.request.user.groups.values("name")
            group = group_queryset[0]["name"]
            context["is_authenticated"] = self.request.user.is_authenticated
            context["is_moderator"] = group in ("moderator", "admin")
            context["is_admin"] = group in ("admin",)
            context["username"] = self.request.user.username
            pk = self.request.user.pk
            user = User.objects.get(user_django__pk=pk)
            context["django_user_pk"] = user.pk
            context["django_user"] = user
        return context


class PaginationMixin:
    """mixin adds pagination to class-based view"""

    def paginated_object(self, queryset: QuerySet) -> QuerySet:
        """function excepts full queryset and return one page"""
        item_list = queryset
        paginator = Paginator(item_list, self.paginate_by)
        page = self.request.GET.get("page")
        return paginator.get_page(page)

    def paginate_page_range(self, total_pages: int, page_number: int) -> list[int]:
        """returns list of pages to display depending on what user's current page"""
        page_range_list = [1]  # first page is always exist

        if total_pages <= 8:
            page_range_list += list(range(2, total_pages + 1))
        elif page_number <= 4:
            page_range_list += [*list(range(2, 7)), None, total_pages]
        elif page_number >= total_pages - 3:
            page_range_list += [None, *list(range(total_pages - 4, total_pages + 1))]
        else:
            middle_range = list(range(page_number - 2, page_number + 3))
            page_range_list += [None, *middle_range, None, total_pages]
        return page_range_list


def funcmixin(request, **kwargs) -> dict:
    """Function that binds logged-in user with its custom model User. Add some consts to context based on group,
    user belong"""
    context = kwargs
    if request.user.is_authenticated:
        group_queryset = request.user.groups.values("name")
        group = group_queryset[0]["name"]
        context["is_authenticated"] = request.user.is_authenticated
        context["is_moderator"] = group in ("moderator", "admin")
        context["is_admin"] = group in ("admin",)
        context["username"] = request.user.username
        pk = request.user.pk
        user = User.objects.get(user_django__pk=pk)
        context["django_user_pk"] = user.pk
    return context
