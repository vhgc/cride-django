""" Users app."""

# Django
from django.apps import AppConfig

class UsersAppConfig(AppConfig):
    """ Users app config."""
    # Nombre de nuestra aplicación es CRIDE porque es el nombre del módulo
    name = 'cride.users'
    verbose_name = 'Users'