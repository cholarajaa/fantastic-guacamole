import datetime
from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import NotificationSerializer, UserSerializer
from .tasks import send_notification


class ListUsers(APIView):
    """
    View to list all users in the system.
    """

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data, status=200)


def index(request):
    return render(
        request,
        'index.html',
        locals()
    )


class NotificationViewSet(viewsets.ViewSet):

    def __init__(self):
        super(NotificationViewSet, self).__init__()
        self.serializer = NotificationSerializer

    def post(self, request):
        send_at = datetime.datetime.strptime(
            request.data['dispatch_time'], "%Y-%m-%d %H:%M:%S")
        payload = {
            'header': request.data['header'],
            'content': request.data['content'],
            'image_url': request.data['image_url']
        }
        send_notification.apply_async(
            (request.data['user_ids'], payload),
            eta=send_at
        )
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response({}, status=400)
