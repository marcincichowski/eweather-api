from django.apps import AppConfig


class eWeatherAPIControllerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'eweather_api_controller'

    def ready(self):
        from .scheduler import scheduler
        scheduler.start()
