from rest_framework.serializers import ModelSerializer, SerializerMethodField
from apps.projects.models import Project
from apps.contributors.models import Contributor
from apps.contributors.serializers import ContributorSerializer
from apps.issues.models import Issue
from apps.issues.serializers import IssueSerializer


class ProjectSerializer(ModelSerializer):
    contributors_count = SerializerMethodField(read_only=True)
    issues_count = SerializerMethodField(read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'proj_type',
                  'issues_count', 'contributors_count')

    def get_contributors_count(self, instance):
        project = instance.id
        count = Contributor.objects.filter(project_id=project).count()
        return count

    def get_issues_count(self, instance):
        project = instance.id
        count = Issue.objects.filter(project_id=project).count()
        return count

    def create(self, validated_data):
        project = super().create(validated_data)
        user = self.context['request'].user
        Contributor.objects.create(project_id_id=project.id, user_id=user,
                                   role='AUTHOR')
        return(project)

    # TODO: voire pour partial update avec PUT


class ProjectDetailSerializer(ModelSerializer):
    contributors = SerializerMethodField(read_only=True)
    issues = SerializerMethodField(read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'proj_type',
                  'issues', 'contributors')

    def get_contributors(self, instance):
        project = instance.id
        queryset = Contributor.objects.filter(project_id=project)
        serializer = ContributorSerializer(queryset, many=True)
        return serializer.data

    def get_issues(self, instance):
        project = instance.id
        queryset = Issue.objects.filter(project_id=project)
        serializer = IssueSerializer(queryset, many=True)
        return serializer.data