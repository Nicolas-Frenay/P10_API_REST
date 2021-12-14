from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from apps.contributors.serializers import ContributorSerializer
from apps.contributors.models import Contributor
from rest_framework.response import Response
from rest_framework.exceptions import NotFound


class UserViewset(ModelViewSet):
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Contributor.objects.filter(project_id=self.kwargs['project_pk'])

    def get_serializer_context(self):
        project = self.kwargs['project_pk']
        context = super(UserViewset, self).get_serializer_context()
        context.update({'project': project})
        context.update({'request': self.request})
        return context

    def destroy(self, request, *args, **kwargs):
        try:
            user = Contributor.objects.get(
                user_id=self.kwargs['pk'],
                project_id_id=self.kwargs['project_pk'])
            user.delete()
            return Response(data='User deleted', status=200)
        except Contributor.DoesNotExist:
            raise NotFound('User not found')