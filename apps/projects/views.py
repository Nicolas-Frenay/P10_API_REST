from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from apps.projects.serializers import ProjectSerializer, \
    ProjectDetailSerializer
from apps.projects.models import Project
from SoftDesk.permissions import IsProjectAuthor, IsProjectContributor


class ProjectViewset(ModelViewSet):
    serializer_class = ProjectSerializer
    detail_serializer_class = ProjectDetailSerializer
    permission_classes = [IsAuthenticated]
    author_permission_classes = [IsAuthenticated, IsProjectAuthor]
    contributor_permission_classes = [IsAuthenticated, IsProjectContributor]

    SAFE_METHODS = ['list']

    def get_queryset(self):
        return Project.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action == 'retrieve':
            self.permission_classes = self.contributor_permission_classes
        elif self.action not in self.SAFE_METHODS:
            self.permission_classes = self.author_permission_classes
        return super().get_permissions()
