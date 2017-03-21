from __future__ import unicode_literals

import mimetypes
import requests

from django.db import models
from django.core.validators import MinValueValidator


def image_validator(url):
    mimetype, encoding = mimetypes.guess_type(url)
    return (mimetype and mimetype.startswith('image'))


def check_url(url):
    """Returns True if the url returns a response code between 200-300,
       otherwise return False.
    """
    try:
        response = requests.get(url)
        return response.status_code in range(200, 209)
    except Exception, ex:
        print ex
        return False


class Notification(models.Model):
    header = models.CharField(
        validators=[MinValueValidator(20)], max_length=150)
    content = models.CharField(
        validators=[MinValueValidator(20)], max_length=150)
    image_url = models.URLField(validators=[image_validator])
    dispatch_time = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def clean(self):
        from django.core.exceptions import ValidationError
        if not image_validator(self.image_url):
            raise ValidationError(
                'must be valid image url, mimetype not image')
        if not check_url(self.image_url):
            raise ValidationError(
                'must be valid image url, response not 2xx')
        if not len(self.header) > 20:
            raise ValidationError(
                'header must be more than 20 characters')
        if not len(self.content) > 20:
            raise ValidationError(
                'content must be more than 20 characters')

    def save(self, *args, **kwargs):
        self.clean()
        super(Notification, self).save(*args, **kwargs)

    def __str__(self):
        return self.image_url
