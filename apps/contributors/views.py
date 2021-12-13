from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from apps.contributors.serializers import ContributorSerializer
from apps.contributors.models import Contributor
from apps.projects.models import Project
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.exceptions import NotFound



class UserViewset(ModelViewSet):
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
        try:
            user = Contributor.objects.get(
                user_id=self.kwargs['pk'],
                project_id_id=self.kwargs['project_pk'])
            user.delete()
            return Response(data='User deleted', status=200)
        except Contributor.DoesNotExist:
            raise NotFound('User not found')