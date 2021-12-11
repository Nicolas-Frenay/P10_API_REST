from rest_framework.serializers import ModelSerializer, SerializerMethodField
from SoftDesk_API.models import Project, Comment, Contributor, Issue


class ProjectListSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description']


class ProjectDetailsSerializer(ModelSerializer):


    project = SerializerMethodField()

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', ]
