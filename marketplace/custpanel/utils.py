from django.core.paginator import Paginator
from django.db.models.query import QuerySet


class PaginationMixin:
    """mixin adds pagination to class-based view"""

    def paginated_object(self, queryset: QuerySet) -> QuerySet:
        """function excepts full queryset and return one page"""
        item_list = queryset
        paginator = Paginator(item_list, self.paginate_by)
        page = self.request.GET.get('page')
        return paginator.get_page(page)

    def paginate_page_range(self, total_pages: int, page_number: int) -> list[int, None]:
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
