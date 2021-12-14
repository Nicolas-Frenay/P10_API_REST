from rest_framework.serializers import ModelSerializer, SerializerMethodField
from apps.issues.models import Issue
from apps.projects.models import Project
from apps.contributors.serializers import UserSerializer


class IssueSerializer(ModelSerializer):
    author_user_id = SerializerMethodField()
    assignee_user_id = SerializerMethodField()

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
    def get_author_user_id(self, instance):
        queryset = instance.author_user_id
        serializer = UserSerializer(queryset)
        return serializer.data

    def get_assignee_user_id(self, instance):
        queryset = instance.assignee_user_id
        serializer = UserSerializer(queryset)
        return serializer.data

    def create(self, validated_data):
        author = self.context['request'].data['author_user_id']
        assignee = self.context['request'].data['assignee_user_id']
        validated_data['author_user_id'] = author
        validated_data['assignee_user_id'] = assignee
        return Issue.objects.create(**validated_data)