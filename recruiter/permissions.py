from rest_framework import permissions

class YearWisePermission(permissions.BasePermission):
    message = 'Junior years have limited access.'
    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True
        
        if request.user.year > 2:
            return True
        
        return False

class SuperUserPermission(permissions.BasePermission):
    message = 'Only superuser can make changes'
    def has_permission(self, request, view):
        
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_superuser:
            return True

        return False