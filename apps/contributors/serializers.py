from rest_framework.serializers import ModelSerializer, \
    SerializerMethodField, ValidationError
from apps.contributors.models import Contributor
from apps.projects.models import Project
from django.contrib.auth.models import User


class ContributorSerializer(ModelSerializer):
    users = SerializerMethodField()

    class Meta:
        model = Contributor
        fields = ('users', 'role')

    def get_users(self, instance):
        queryset = instance.user_id
        serializer = UserSerializer(queryset)
        return serializer.data

    def create(self, validated_data):
        new_username = self.context['request'].data['new_user']
        role = self.context['request'].data['role']
        project_id = self.context['project']
        project = Project.objects.get(id=project_id)

        try:
            new_user = User.objects.get(username=new_username)
            try:
                if Contributor.objects.get(project_id=project,
                                           user_id=new_user):
                    raise ValidationError(
                        'User already working on this project')
            except Contributor.DoesNotExist:
                contrib = Contributor.objects.create(project_id=project,
                                                     role=role,
                                                     user_id=new_user)
                return contrib
        except User.DoesNotExist:
            raise ValidationError('Invalid user name')


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')
