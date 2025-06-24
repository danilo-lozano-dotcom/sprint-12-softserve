from django.apps import AppConfig

class AppointmentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appointments' # Nombre de la app, debe coincidir con el nombre del directorio de la app