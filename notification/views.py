from django.shortcuts import render
from rest_framework import generics
from .serializers import NotificationSerializer
from .models import Notification


class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Notification."""
        serializer.save()
