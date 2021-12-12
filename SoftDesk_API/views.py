from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from SoftDesk_API.models import Project, Contributor, Comment, Issue
from SoftDesk_API.serializers import ProjectListSerializer, \
    ProjectDetailsSerializer, RegisterSerializer, UserSerializer, ContributorSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User


# class MultipleSerializerMixin:
#     detail_serializer_class = None
#
#     def get_serializer_class(self):
#         if self.action == 'retrieve' and self.detail_serializer_class:
#             return self.detail_serializer_class
#         return super().get_serializer_class()


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    # permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class ProjectViewset(ModelViewSet):
    serializer_class = ProjectListSerializer
    detail_serializer_class = ProjectDetailsSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.all()

    @action(detail=True)
    def users(self, request, pk):
        project = self.get_object()
        serializer = ContributorSerializer
        # queryset = User.objects.filter(
        #     id__in=(
        #         Contributor.objects.filter(project_id=project.id).values_list(
        #             'user_id')))
        # return Response(UserSerializer(queryset, many=True).data)
        queryset = Contributor.objects.filter(project_id=project.id)
        return Response(serializer(queryset, many=True).data)
