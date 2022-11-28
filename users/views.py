from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UsersListSerializer
from django.contrib.auth.models import User


class RegisterAPIView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UsersListSerializer
    permission_classes = AllowAny

