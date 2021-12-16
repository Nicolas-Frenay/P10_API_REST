from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User
from apps.contributors.models import Contributor


class IsProjectAuthor(BasePermission):
    def has_permission(self, request, view):
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
        project = request.parser_context['kwargs']['pk']
        if Contributor.objects.filter(user_id=request.user.id,
                                      project_id=project):
            return True
        return False
