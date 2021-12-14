from rest_framework.serializers import ModelSerializer, \
    SerializerMethodField, ValidationError
from rest_framework.validators import UniqueTogetherValidator
from apps.contributors.models import Contributor
from django.core.exceptions import NON_FIELD_ERRORS
from django.contrib.auth.models import User


class ContributorSerializer(ModelSerializer):
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

    def create(self, validated_data):
        if User.objects.filter(id=self.context['request'].data['user_id']):
            new_user = User.objects.get(
                id=self.context['request'].data['user_id'])
            validated_data['user_id'] = new_user
            return Contributor.objects.create(**validated_data)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')
