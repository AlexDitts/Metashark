from rest_framework import permissions


class AdministratorPermission(permissions.BasePermission):
    """
    Класс permission разрешающий доступ к представлению только пользователям состоящим в группе администратор.
    """

    def has_permission(self, request, view):
        return request.user.groups.filter(name='Administrator')


class CuratorPermission(permissions.BasePermission):
    """
    Класс permission разрешающий доступ к представлению только пользователям состоящим в группе куратор.
    """

    def has_permission(self, request, view):
        return bool(request.user.groups.filter(name='Curator').first())
