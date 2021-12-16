from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User
from apps.contributors.models import Contributor


class IsProjectAuthor(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        project = request.parser_context['kwargs']['pk']
        if Contributor.objects.filter(user_id=request.user.id,
                                      project_id=project):
            user = Contributor.objects.get(user_id=request.user.id,
                                           project_id=project)
            if user.role == 'AUTHOR':
                return True
        return False



class IsProjectContributor(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        try:
            project = request.parser_context['kwargs']['project_pk']
        except:
            project = request.parser_context['kwargs']['pk']
        if Contributor.objects.filter(user_id=request.user.id,
                                      project_id=project):
            return True
        return False

class IsIssueAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if obj.author_user_id == request.user:
            return True
        return False