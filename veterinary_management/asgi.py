import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'veterinary_management.settings')

application = get_asgi_application() # Punto de entrada para servidores ASGI