#!/home/abc/.pyenv/versions/3.4.3/bin/python3.4
"""
WSGI config for qofc project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""
# #!/home/abc/.pyenv/versions/3.4.3/bin/python3.4

import os
import sys

source_dir = os.path.dirname(__file__)
if not source_dir in sys.path:
    sys.path.insert(0, source_dir)

from utils.config import Config
from django.core.wsgi import get_wsgi_application

settings_module = Config.get('config', 'main', 'settings_module', default='settings.production')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

application = get_wsgi_application()
