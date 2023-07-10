from rest_framework import permissions

class IsEventCreator(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow only the event creator to edit or delete the event
        return obj.creator == request.user

class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow only admin users to perform actions
        return request.user.is_staff
