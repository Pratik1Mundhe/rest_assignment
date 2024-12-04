from django.apps import AppConfig

class RestAppAppConfig(AppConfig):
    name = "rest_app"

    def ready(self):
        from rest_app import signals # pylint: disable=unused-variable
