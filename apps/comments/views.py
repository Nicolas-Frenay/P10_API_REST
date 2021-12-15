from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from apps.comments.serializers import CommentSerializer
from apps.comments.models import Comment


class CommentViewset(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(issue_id=self.kwargs['issue_pk'])

    def get_serializer_context(self):
        if self.action == 'create':
            issue = self.kwargs['issue_pk']
            user = self.request.user
            context = super(CommentViewset, self).get_serializer_context()
            context['request'].data._mutable = True
            context['request'].data.update({'author_user_id': user})
            context['request'].data.update({'issue_id': issue})
            return context