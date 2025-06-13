"""
Serializers for the user API View
"""
from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    """Serializers for the user object"""

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwargs = {'password': {
            'write_only': True,
            'min_length': 5
        }}

    def create(self, validated_data):
        """create and return the user with enc. data"""
        return get_user_model().objects.create_user(**validated_data)
