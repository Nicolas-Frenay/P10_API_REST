from rest_framework.generics import CreateAPIView
from apps.authentication.serializers import RegisterSerializer
from django.contrib.auth.models import User

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer