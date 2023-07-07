from django.apps import AppConfig


class EmsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ems'

    def ready(self):
        import ems.signals
