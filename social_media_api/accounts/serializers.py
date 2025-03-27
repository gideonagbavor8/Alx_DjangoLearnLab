from rest_framework import serializers
# from accounts.models import CustomUser
from rest_framework.authtoken.models import Token

from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'followers': {'read_only': True},  # Prevents "followers" from being required
        }

    def create(self, validated_data):
        # Use get_user_model() to create a user
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
        )
        Token.objects.create(user=user)  # Generate a token for the user upon registration
        return user




class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
