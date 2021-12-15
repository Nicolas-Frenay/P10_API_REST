from rest_framework.serializers import ModelSerializer, SerializerMethodField
from apps.issues.models import Issue
from apps.contributors.serializers import UserSerializer
from django.contrib.auth.models import User


class IssueSerializer(ModelSerializer):
    author = SerializerMethodField()
    assignee = SerializerMethodField()

    class Meta:
        model = Issue
        fields = (
            'id',
            'project_id',
            'title',
            'created_time',
            'tag',
            'priority',
            'status',
            'desc',
            'author',
            'assignee'
        )

    def get_user(self, instance):
        queryset = User.objects.get(id=instance.id)
        serializer = UserSerializer(queryset)
        return serializer.data

    def get_author(self, instance):
        return self.get_user(instance.author_user_id)

    def get_assignee(self, instance):
        return self.get_user(instance.assignee_user_id)

class IssueCreateSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = (
            'id',
            'project_id',
            'title',
            'created_time',
            'tag',
            'priority',
            'status',
            'desc',
            'author_user_id',
            'assignee_user_id'
        )
