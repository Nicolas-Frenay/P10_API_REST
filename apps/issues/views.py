from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from apps.issues.serializers import IssueSerializer
from apps.issues.models import Issue
from django.contrib.auth.models import User


class IssueViewset(ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Issue.objects.filter(project_id=self.kwargs['project_pk'])

    def get_serializer_context(self):
        if self.action == 'create':
            project = self.kwargs['project_pk']
            user = self.request.user.id
            context = super(IssueViewset, self).get_serializer_context()
            context['request'].data._mutable = True
            context['request'].data.update({'project_id': project})
            context['request'].data.update({'author_user_id': user})
            context['request'].data.update({'assignee_user_id':user})
            return context
