from django.apps import AppConfig

import signals


class SignalsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "signals"

    def ready(self):
        import signals.signals
