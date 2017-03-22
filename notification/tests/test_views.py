import datetime

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError


class ViewTestCase(TestCase):
    """Test suite for api views."""

    def setUp(self):
        """
        Define the test client and notification data
        """
        url = 'https://static.pexels.com/photos/7720/night-animal-dog-pet.jpg'
        dispatch_time = "2017-03-22 06:01:32"
        self.client = APIClient()
        self.notification_data = {
            'header': 'some header to show this',
            'content': 'this is some content to be shows',
            'image_url': url,
            'dispatch_time': dispatch_time,
            'user_ids': [1, 2]
        }

    def test_api_can_create_notification(self):
        """
        Test the api has notification created.
        """
        self.response = self.client.post(
            reverse('notifications'),
            self.notification_data,
            format="json"
        )
        self.assertEqual(
            self.response.status_code,
            status.HTTP_201_CREATED
        )

    def test_api_fail_to_create_notification(self):
        """
        Test the api has notification created.
        """
        del self.notification_data['header']
        # try:
        self.response = self.client.post(
            reverse('notifications'),
            self.notification_data,
            format="json"
        )
        self.assertEqual(
            self.response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
        # except Exception as e:
        #     self.assertEqual(
        #         [u'header must be more than 20 characters'],
        #         e.messages
        #     )
