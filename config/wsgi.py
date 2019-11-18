"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.pycharm')
if os.environ.get('ON_HEROKU'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.heroku')


application = get_wsgi_application()

application = get_wsgi_application()
