from rest_framework.permissions import BasePermission
from apps.contributors.models import Contributor


class IsProjectAuthor(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        # Depending of the endpoint's URL, the project's pk is pass under a
        # different key
        try:
            project = request.parser_context['kwargs']['project_pk']
        except:
            project = request.parser_context['kwargs']['pk']

        # check if there is a contributor object for this user and this project
        if Contributor.objects.filter(user_id=request.user.id,
                                      project_id=project):
            user = Contributor.objects.get(user_id=request.user.id,
                                           project_id=project)
        # check if the user is the project author
            if user.permissions == 'AUTHOR':
                return True
        return False


class IsProjectContributor(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        # Depending of the endpoint's URL, the project key is pass under a
        # different key
        try:
            project = request.parser_context['kwargs']['project_pk']
        except:
            project = request.parser_context['kwargs']['pk']
        if Contributor.objects.filter(user_id=request.user.id,
                                      project_id=project):
            return True
        return False

class IsAuthor(BasePermission):
    """
    Permission that check if request.user is author of an issue or a comment
    """
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if obj.author_user_id == request.user:
            return True
        return False
