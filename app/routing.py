from django.urls import re_path

import app.consumers as consumers

websocket_urlpatterns = [
    re_path(r"ws/guess/$", consumers.ChatConsumer.as_asgi()),
]