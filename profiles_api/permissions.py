from  rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit thier own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying ti edi theor own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id  == request.user.id
        
