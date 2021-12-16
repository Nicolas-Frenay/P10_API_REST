from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from apps.issues.serializers import IssueSerializer, IssueCreateSerializer
from apps.issues.models import Issue
from SoftDesk.permissions import IsProjectContributor, IsAuthor
from rest_framework.exceptions import MethodNotAllowed


class IssueViewset(ModelViewSet):
    serializer_class = IssueSerializer
    create_serializer = IssueCreateSerializer
    permission_classes = [IsAuthenticated, IsProjectContributor]
    author_permission_classes = [IsAuthenticated, IsProjectContributor,
                                 IsAuthor]

    SAFE_METHODS = ['list']

    def get_queryset(self):
        return Issue.objects.filter(project_id=self.kwargs['project_pk'])

    def get_serializer_class(self):
        if self.action == 'create':
            return self.create_serializer
        return super().get_serializer_class()

    def get_serializer_context(self):
        if self.action == 'create':
            project = self.kwargs['project_pk']
            user = self.request.user
            context = super(IssueViewset, self).get_serializer_context()
            context['request'].data._mutable = True
            context['request'].data.update({'project_id': project})
            context['request'].data.update({'author_user_id': user.id})
            context['request'].data.update({'assignee_user_id': user.id})
            return context

    def get_permissions(self):
        if self.action not in self.SAFE_METHODS:
            self.permission_classes = self.author_permission_classes
        return super().get_permissions()

    def retrieve(self, request, *args, **kwargs):
        raise MethodNotAllowed('GET',
                               detail='Method "GET" not allowed with lookup '
                                      'on this endpoint')
