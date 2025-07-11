from rest_framework import serializers
from apps.users.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)