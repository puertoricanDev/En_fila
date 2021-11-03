from django.urls import re_path

from ..apps.mi_fila import consumers

websocket_urlpatterns = [
    re_path(r'(?P<area_id>\w+)/$', consumers.En_filaConsumer.as_asgi()),
]
