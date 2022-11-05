from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializers(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, required=True,
                                     validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)


class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {
                    "password": "Password field didn't match"
                }
            )
        return attrs

    def create(self, validate_data):
        validate_data.pop('password2')
        user = User.objects.create_user(
            validate_data.pop('username'),
            password=validate_data.pop('password')
        )
        return user

