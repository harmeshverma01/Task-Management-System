from rest_framework.permissions import BasePermission


class admin_required(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'admin':
            return True
        return False
    
class Manager_required(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'manager':
            return True
        return False


    

