"""
ASGI config for sound project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from uvicorn.workers import UvicornWorker as BaseUvicornWorker


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sound.settings')

application = get_asgi_application()


class UvicornWorker(BaseUvicornWorker):
    # Выключаем lifespan потому что Django с ним не работает
    CONFIG_KWARGS = {'lifespan': 'off'}
