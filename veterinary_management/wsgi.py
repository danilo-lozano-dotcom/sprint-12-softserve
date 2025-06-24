import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'veterinary_management.settings')

application = get_wsgi_application() # Punto de entrada para servidores WSGI