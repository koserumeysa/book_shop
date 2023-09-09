from rest_framework import permissions
from pprint import pprint


# SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    #If it is a safe method, we allow everybody to access the api.
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        #If it is a safe method, we allow everybody to access the api.
        return request.method in permissions.SAFE_METHODS or is_admin

class IsCommenterOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #If it is a safe method, we allow everybody to access the api.
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.commenter == request.user
       