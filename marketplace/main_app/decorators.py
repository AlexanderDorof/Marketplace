# from django.http import HttpResponseForbidden
#
# def is_moderator(view_func):
#     """
#     Декоратор, который проверяет, является ли пользователь модератором.
#     """
#     def _wrapped_view(request, *args, **kwargs):
#         if request.user.is_authenticated and request.user.groups.filter(name='moderator').exists():
#             return view_func(request, *args, **kwargs)
#         else:
#             return HttpResponseForbidden("Только модераторы имеют доступ к этой странице.")
#     return _wrapped_view
