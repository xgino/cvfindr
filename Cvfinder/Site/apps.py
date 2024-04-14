from django.apps import AppConfig
from django.db.models.signals import post_migrate

class SiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Site'

    def ready(self):
        # Import your signals here
        from .signals import create_initial_records

        # Connect signals
        post_migrate.connect(create_initial_records, sender=self)