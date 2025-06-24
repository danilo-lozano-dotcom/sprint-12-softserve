from django.apps import AppConfig

class OwnersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'owners' # Nombre de la app, debe coincidir con el nombre del directorio