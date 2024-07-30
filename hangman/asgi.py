"""
WSGI config for hangman project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

For more information, visit
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
from django.core.asgi  import get_asgi_application
from django import setup
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'hangman.settings')
setup()


from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.routing import ProtocolTypeRouter

from channels.auth import AuthMiddlewareStack


django_asgi_app = get_asgi_application()
# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.

import app.routing

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(app.routing.websocket_urlpatterns))
    ),
})


