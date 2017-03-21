from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    """
    Serializer to map the Model instance into JSON format.
    """
    class Meta:
        """
        Meta class to map serializer's fields with the model fields.
        """
        model = Notification
        fields = ('header', 'content', 'image_url',
                  'dispatch_time', 'created_date', 'modified_date')
        read_only_fields = ('created_date', 'modified_date')


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer to map the Model instance into JSON format.
    """
    class Meta:
        """
        Meta class to map serializer's fields with the model fields.

        """ 
        model = User
        fields = ('id', 'username')
