"""publican_api utilities"""

import publican_api as api


def get_app_label():
    return api.__app_label__


def get_api_version():
    return api.__version__


def get_entity_regex(entity_superclass=None):
    models = []
    for entity in dir(api.models):
        try:
            model = getattr(api.models, entity)
            if issubclass(model, entity_superclass):
                models.append(model._meta.verbose_name_plural)
        except:
            pass
    model_name = entity_superclass.__name__.lower()
    return "^(?P<" + model_name + ">(" + "|".join(models) + "))/"