from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'(?P<area_id>\w+)/$', consumers.En_filaConsumer.as_asgi()),
]
