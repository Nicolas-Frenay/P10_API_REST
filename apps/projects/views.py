from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from apps.projects.serializers import ProjectListSerializer, ProjectDetailsSerializer
from apps.projects.models import Project
from apps.contributors.models import Contributor

class ProjectViewset(ModelViewSet):
    serializer_class = ProjectListSerializer
    detail_serializer_class = ProjectDetailsSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        serializer = ProjectDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            id = serializer.data['id']
            contributor = Contributor.objects.create(project_id_id=id,
                                                     role='AUTHOR')
            contributor.user_id.set([request.user.id, ])
            contributor.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def update(self, request, *args, **kwargs):
        project = self.get_object()
        serializer = ProjectDetailsSerializer(project, data=request.data,
                                              partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
