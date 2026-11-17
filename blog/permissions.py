from rest_framework import permissions

class IsWriterOrReadOnly(permissions.BasePermission):         # class is inheriting base permission to be identified by DRF. 

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:        #checks if the user is here to read only, or use get. 
            return True
        
        return bool(request.user and request.user.is_authenticated and request.user.role == 'writer')     # Authorization checks when user wants to put, delete, create new post.

    def has_object_permission(self, request, view, obj): 
        if request.method in permissions.SAFE_METHODS:      # any reader or not authorized reader can read or get any specific post (obj)
            return True

        return obj.author == request.user        # checks if the user that is trying to edit or delete the post is author of it. 

    