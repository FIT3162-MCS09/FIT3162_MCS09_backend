# models/apps.py
from django.apps import AppConfig

class ModelsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'models'

    def ready(self):
        # Import models here to avoid AppRegistryNotReady error
        from . import file