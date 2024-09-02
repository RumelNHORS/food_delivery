from rest_framework.permissions import BasePermission

# IsOwnerOrEmployee ensures that only authenticated users who are either owners or employees can access certain views.
class IsOwnerOrEmployee(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.is_owner or request.user.is_employee)
