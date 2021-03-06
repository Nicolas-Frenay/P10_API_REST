from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework.validators import UniqueTogetherValidator
from apps.contributors.models import Contributor
from django.contrib.auth.models import User


class ContributorSerializer(ModelSerializer):
    """
    Display contributor serializer
    """
    user = SerializerMethodField()

    class Meta:
        model = Contributor
        fields = ('project_id', 'user_id', 'user', 'role')
        validators = [
            UniqueTogetherValidator(
                queryset=Contributor.objects.all(),
                fields=['user_id', 'project_id'],
                message='User already working on that project'
            )
        ]

    def get_user(self, instance):
        queryset = instance.user_id
        serializer = UserSerializer(queryset)
        return serializer.data


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')
