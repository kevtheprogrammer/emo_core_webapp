from rest_framework import serializers
from .models import *


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'email',   'groups')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
