from rest_framework.serializers import ModelSerializer, SerializerMethodField
from apps.contributors.models import Contributor
from django.contrib.auth.models import User


class ContributorSerializer(ModelSerializer):
    users = SerializerMethodField()

    class Meta:
        model = Contributor
        fields = ('users', 'role')

    def get_users(self, instance):
        queryset = instance.user_id
        serializer = UserSerializer(queryset, many=True)
        return serializer.data


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')