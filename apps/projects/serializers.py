from rest_framework.serializers import ModelSerializer
from apps.projects.models import Project
from apps.contributors.models import Contributor


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

    def create(self, validated_data):
        project = super().create(validated_data)
        user = self.context['request'].user
        Contributor.objects.create(project_id_id=project.id, user_id=user,
                                   role='AUTHOR')
        return(project)

    # TODO: voire pour partial update avec PUT
