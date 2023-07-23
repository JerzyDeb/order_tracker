"""Api utils."""
# Standard Library
import importlib

from django.apps import apps
# Django
from django.conf import settings


def get_serializer_class():
    serializer_path = settings.ORDER_SERIALIZER.split('.')
    serializer_name = serializer_path[-1]
    del serializer_path[-1]
    serializer_module = importlib.import_module('.'.join(serializer_path))
    serializer_class = getattr(serializer_module, serializer_name)
    return serializer_class


def get_model_objects(user):
    model_path = settings.ORDER_MODEL.split('.')
    model_name = model_path[-1]
    del model_path[-1]
    model = apps.get_model('.'.join(model_path), model_name)
    lookup_expr = {
        settings.FK_TO_USER: user
    }
    return model.objects.filter(**lookup_expr)
