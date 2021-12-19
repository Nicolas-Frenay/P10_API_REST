from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from apps.comments.serializers import CommentSerializer, \
    CommentCreateSerializer
from apps.comments.models import Comment
from SoftDesk.permissions import IsProjectContributor, IsAuthor
from rest_framework.exceptions import MethodNotAllowed


class CommentViewset(ModelViewSet):
    serializer_class = CommentSerializer
    create_serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated, IsProjectContributor]
    author_permission_classes = [IsAuthenticated, IsProjectContributor,
                                 IsAuthor]

    SAFE_METHODS = ['list', 'create']

    def get_queryset(self):
        return Comment.objects.filter(issue_id=self.kwargs['issue_pk'])

    def get_serializer_class(self):
        methods = ('create', 'update', 'partial_update')
        if self.action in methods:
            return self.create_serializer_class
        return super().get_serializer_class()

    def get_serializer_context(self):
        if self.action == 'create':
            issue = self.kwargs['issue_pk']
            user = self.request.user
            context = super(CommentViewset, self).get_serializer_context()
            context['request'].data._mutable = True
            context['request'].data.update({'author_user_id': user.id})
            context['request'].data.update({'issue_id': issue})
            return context

    def get_permissions(self):
        if self.action not in self.SAFE_METHODS:
            self.permission_classes = self.author_permission_classes
        return super().get_permissions()

    def retrieve(self, request, *args, **kwargs):
        raise MethodNotAllowed('GET',
                               detail='Method "GET" not allowed with lookup '
                                      'on this endpoint')
