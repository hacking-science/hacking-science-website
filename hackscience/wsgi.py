"""
WSGI config for hackscience project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

if os.environ.get('APP_ENV',None)=='prod':
    path = '/home/ubuntu/hacking-science-website'
    if path not in sys.path:
        sys.path.append(path)


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hackscience.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
