"""
WSGI config for smart_carpark project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from smart_carpark.anpr_db_update import anpr_db_updater

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smart_carpark.settings')

application = get_wsgi_application()
anpr_db_updater()
