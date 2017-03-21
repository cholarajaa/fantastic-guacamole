import datetime

from django.test import TestCase
from ..models import Notification


class NotificationTestCase(TestCase):
    """
    This class defines the test suite for
    the Notification model
    """

    def setUp(self):
        """Define Model variables"""
        self.header = 'some header to show this'
        self.content = 'this is some content to be shows'
        self.image_url = 'https://static.pexels.com/photos/7720/' +\
            'night-animal-dog-pet.jpg'
        self.dispatch_time = datetime.datetime.now() +\
            datetime.timedelta(hours=1)
        self.notification = Notification(
            header=self.header,
            content=self.content,
            image_url=self.image_url,
            dispatch_time=self.dispatch_time
        )

    def test_model_can_create_notification(self):
        """
        Test Notification model can create a Notificaiton
        """
        old_count = Notification.objects.count()
        self.notification.save()
        new_count = Notification.objects.count()
        self.assertNotEqual(old_count, new_count)
