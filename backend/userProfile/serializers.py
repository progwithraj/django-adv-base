from .models import UserProfile
from rest_framework import serializers


class UserProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True},  # The user field should be read-only
        }
