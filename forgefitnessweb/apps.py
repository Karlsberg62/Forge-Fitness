from django.apps import AppConfig


class ForgefitnesswebConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'forgefitnessweb'

    def ready(self):
        import forgefitnessweb.signals
