from rest_framework.serializers import ModelSerializer, SerializerMethodField
from apps.comments.models import Comment


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'author_user_id', 'issue_id', 'created_time', 'description')

