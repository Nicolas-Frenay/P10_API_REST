from rest_framework.serializers import ModelSerializer, SerializerMethodField
from apps.comments.models import Comment
from apps.contributors.serializers import UserSerializer


class CommentCreateSerializer(ModelSerializer):
    """
    Creating comment serializer
    """
    class Meta:
        model = Comment
        fields = ('id', 'author_user_id', 'issue_id', 'created_time', 'description')


class CommentSerializer(ModelSerializer):
    """
    Display comment serializer
    """
    author = SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'author', 'issue_id', 'created_time', 'description')


    def get_author(self, instance):
        user = instance.author_user_id
        serializer = UserSerializer(user)
        return serializer.data