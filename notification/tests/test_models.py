import datetime

from django.test import TestCase
from django.core.exceptions import ValidationError
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


    def test_model_validation_error_on_invalid_image_url(self):
        try:
            self.notification.image_url = 'asdf.dd'
            self.notification.save()
        except Exception as e:
            self.assertEqual(
                [u'must be valid image url, mimetype not image'],
                e.messages
            )


    def test_model_validation_error_on_invalid_image_response(self):
        try:
            self.notification.image_url = 'https://stic.pexels.com/' +\
                'photos/7720/night-animal-dog-pet.jpg'
            self.notification.save()
        except Exception as e:
            self.assertEqual(
                'must be valid image url, response not 2xx',
                e.message
            )
