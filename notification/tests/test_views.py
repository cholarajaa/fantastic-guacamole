import datetime

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse


class ViewTestCase(TestCase):
    """Test suite for api views."""

    def setUp(self):
        """
        Define the test client and notification data
        """
        url = 'https://static.pexels.com/photos/7720/night-animal-dog-pet.jpg'
        dispatch_time = datetime.datetime.now()\
            + datetime.timedelta(hours=1)
        self.client = APIClient()
        self.notification_data = {
            'header': 'some header to show this',
            'content': 'this is some content to be shows',
            'image_url': url,
            'dispatch_time': dispatch_time
        }
        self.response = self.client.post(
            reverse('create'),
            self.notification_data,
            format="json"
        )

    def test_api_can_create_notification(self):
        """
        Test the api has notification created.
        """
        self.assertEqual(
            self.response.status_code,
            status.HTTP_201_CREATED
        )
