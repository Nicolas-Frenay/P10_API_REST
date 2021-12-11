from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from SoftDesk_API.models import Project
from SoftDesk_API.serializers import ProjectListSerializer, ProjectDetailsSerializer, RegisterSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User


class MultipleSerializerMixin:
    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class:
            return self.detail_serializer_class
        return super().get_serializer_class()


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    # permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class ProjectListViewset(ModelViewSet, MultipleSerializerMixin):
    serializer_class = ProjectListSerializer
    detail_serializer_class = ProjectDetailsSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.all()