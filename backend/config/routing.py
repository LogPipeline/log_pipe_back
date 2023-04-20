from django.urls import path 
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from . import consumer

websocket_urlpatterns = [
    path("ws/data/", consumer.MyConsumer.as_asgi())
]


application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})