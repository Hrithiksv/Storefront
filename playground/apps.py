"""
Module level docstring explaining the purpose of the module and any important details.
"""
from django.apps import AppConfig


class PlaygroundConfig(AppConfig):
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'playground'
