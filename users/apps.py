from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    #imports the signals for the profile creation and update, as shown in the django documentation
    def ready(self):
        import users.signals