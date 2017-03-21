from __future__ import absolute_import

import os

from celery import Celery
from django.conf import settings
from notifier import celeryconfig

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notifier.settings')

app = Celery('notifier')


app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.config_from_object('notifier:celeryconfig')
