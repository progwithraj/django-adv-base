from django.apps import AppConfig


class UserprofileConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "userProfile"

    # this method is called when the app is ready and the signals are connected
    def ready(self):
        import userProfile.signals  # noqa
