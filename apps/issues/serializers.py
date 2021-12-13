from rest_framework.serializers import ModelSerializer, SerializerMethodField
from apps.issues.models import Issue
from apps.users.serializers import UserSerializer


class IssueDetailsSerializer(ModelSerializer):
    author = SerializerMethodField()
    assignee = SerializerMethodField()

    class Meta:
        model = Issue
        fields = (
            'title',
            'created_time',
            'tag',
            'priority',
            'status',
            'author',
            'assignee'
        )
    def get_author(self, instance):
        queryset = instance.author_user_id
        serializer = UserSerializer(queryset)
        return serializer.data

    def get_assignee(self, instance):
        queryset = instance.assignee_user_id
        serializer = UserSerializer(queryset)
        return serializer.data

class IssueListSerialize(ModelSerializer):
    class Meta:
        model = Issue
        fields = ('title', 'tag', 'priority', 'status')