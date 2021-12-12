from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from SoftDesk_API.models import Project, Contributor, Comment, Issue
from SoftDesk_API.serializers import ProjectListSerializer, \
    ProjectDetailsSerializer, RegisterSerializer, ContributorSerializer
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

    # @action(detail=True, methods=['post'])
    def create(self, request, *args, **kwargs):
        serializer = ProjectDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            id = serializer.data['id']
            Contributor.objects.create(user_id=request.user.id,
                                       project_id_id=id, role='AUTHOR')
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    @action(detail=True, methods=['get', 'post'])
    def users(self, request, pk):
        if request.method == 'GET':
            project = self.get_object()
            serializer = ContributorSerializer
            queryset = Contributor.objects.filter(project_id=project.id)
            return Response(serializer(queryset, many=True).data)

        if request.method == 'POST':
            project = self.get_object()
            data = request.data
            new_username = data['new_user']
            try:
                new_user = User.objects.get(username=new_username)
                contrib = Contributor.objects.create(user_id=new_user.id,
                                                     project_id=project,
                                                     role='CONTRIBUTOR')
                contrib.save()
                return Response(data='New user added', status=200)
            except User.DoesNotExist:
                raise NotFound('Invalid user name')
