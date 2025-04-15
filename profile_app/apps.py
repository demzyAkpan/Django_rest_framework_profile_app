from django.apps import AppConfig


class ProfileAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profile_app'

    def ready(self):
        import profile_app.signals
        # This will ensure that the signals are imported when the app is ready
        # and that the signal handlers are connected to the appropriate signals.
        # This is important for ensuring that the signals work correctly.
        # The import statement is placed here to avoid circular imports.
