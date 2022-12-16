from django.http import Http404
from rest_framework.permissions import BasePermission

from ads.models import Comment, Ad
from users.models import User


# TODO здесь производится настройка пермишенов для нашего проекта
class PermissionsForUserAds(BasePermission):
    message = 'Изменять или удалять объявления  могут только создатель  или Админ'

    def has_permission(self, request, view):
        try:
            obj = Ad.objects.get(pk=view.kwargs['pk'])
        except Ad.DoesNotExist:
            raise Http404
        if obj.author_id == request.user.id or request.user.role == 'admin':
            return True
        return False


class PermissionsForUserComments(BasePermission):
    message = 'Изменять или удалять комментарии могут только создатель  или Админ'

    def has_permission(self, request, view):
        try:
            obj = Comment.objects.get(pk=view.kwargs['id'])
        except Comment.DoesNotExist:
            raise Http404
        print(obj.author_id)
        if obj.author_id == request.user.pk or request.user.role == 'admin':
            return True
        return False


class IsAdminPermissions(BasePermission):
    message = 'Удалять или редактировать чужие объявления и комментарии могут только Админы'

    def has_permission(self, request, view):
        try:
            obj = User.objects.get(pk=request.user.pk)
        except User.DoesNotExist:
            raise Http404
        if obj.role == 'admin':
            return True
        return False

