from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from SoftDesk_API.models import Project, Contributor, Comment, Issue
from SoftDesk_API.serializers import ProjectListSerializer, \
    ProjectDetailsSerializer, RegisterSerializer, ContributorSerializer, \
    UserSerializer
from rest_framework.permissions import IsAuthenticated


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    # permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


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


class ProjectUserViewset(ModelViewSet):
    serializer_class = ContributorSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Contributor.objects.filter(project_id=self.kwargs['project_pk'])

    def create(self, request, *args, **kwargs):
        new_username = request.data['new_user']
        project = Project.objects.get(id=self.kwargs['project_pk'])
        try:
            new_user = User.objects.get(username=new_username)
            contrib = Contributor.objects.create(project_id=project,
                                                 role='CONTRIBUTOR')
            contrib.user_id.set([new_user.id, ])
            contrib.save()
            return Response(data='New user added', status=200)
        except User.DoesNotExist:
            raise NotFound('Invalid user name')

    def destroy(self, request, *args, **kwargs):
        #TODO renvois pas d'erreur si contrib déjà effacé
        try:
            user = Contributor.objects.get(
                user_id=self.kwargs['pk'],
                project_id_id=self.kwargs['project_pk'])
            user.delete()
            return Response(data='User deleted', status=200)
        except Contributor.DoesNotExist:
            raise NotFound('User not found')