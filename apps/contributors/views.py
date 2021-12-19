from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from apps.contributors.serializers import ContributorSerializer
from apps.contributors.models import Contributor
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, MethodNotAllowed
from SoftDesk.permissions import IsProjectContributor, IsProjectAuthor


class UserViewset(ModelViewSet):
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated, IsProjectContributor]
    author_permission_classes = [IsAuthenticated, IsProjectAuthor]

    def get_queryset(self):
        return Contributor.objects.filter(project_id=self.kwargs['project_pk'])

    def get_serializer_context(self):
        """
        overridden method to add author and issue id in context
        :return:  updated context
        """
        if self.action == 'create':
            project = self.kwargs['project_pk']
            context = super(UserViewset, self).get_serializer_context()
            user_id = context['request'].data['new_user']
            context['request'].data._mutable = True
            context['request'].data.update({'project_id': project})
            context['request'].data.update({'user_id': user_id})
            return context

    def destroy(self, request, *args, **kwargs):
        """
        overridden methode to check is contributor exist, and send custom
        response if it doesn't
        :return: http response
        """
        try:
            user = Contributor.objects.get(
                user_id=self.kwargs['pk'],
                project_id_id=self.kwargs['project_pk'])
            user.delete()
            return Response(data='User deleted', status=200)
        except Contributor.DoesNotExist:
            raise NotFound('User not found')

    def get_permissions(self):
        if self.action =='destroy' :
            self.permission_classes = self.author_permission_classes
        return super().get_permissions()

    def retrieve(self, request, *args, **kwargs):
        """
        Overridden method to block un-authorize request method
        """
        raise MethodNotAllowed('GET',
                               detail='Method "GET" not allowed with lookup '
                                      'on this endpoint')

    def update(self, request, *args, **kwargs):
        """
        Overridden method to block un-authorize request method
        """
        raise MethodNotAllowed('PUT',
                               detail='Method "PUT" not allowed on this '
                                      'endpoint')

    def partial_update(self, request, *args, **kwargs):
        """
        Overridden method to block un-authorize request method
        """
        raise MethodNotAllowed('PATCH',
                               detail='Method "PATCH" not allowed on this '
                                      'endpoint')