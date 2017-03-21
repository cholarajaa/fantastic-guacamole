from django.conf.urls import url
from .views import index, ListUsers, NotificationViewSet
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = {
    url(r'^$', index, name="index"),
    url(r'^users/$', ListUsers.as_view(), name="users"),
    url(r'^notifications/$', NotificationViewSet.as_view(
        {'get': 'post', 'post': 'post'}), name="notifications")
}

urlpatterns = format_suffix_patterns(urlpatterns)
