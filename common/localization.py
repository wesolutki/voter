import re
import inspect
from django.utils.translation import ugettext as txt
from django.utils.translation import gettext_lazy
from django.utils import six  # Python 3 compatibility
from django.utils.functional import lazy
from django.utils.translation import force_text


def camelcase_to_underscore(string):
    return re.sub('(((?<=[a-z])[A-Z0-9])|([A-Z0-9](?![A-Z0-9]|$)))', '_\\1', string).lower().strip('_')


# noinspection PyProtectedMember
def verbose_names(model):
    app_name = camelcase_to_underscore(model.__module__.split('.')[0])
    text = camelcase_to_underscore(model.__name__)
    for field in model._meta.fields:
        setattr(field, 'verbose_name', txt(field.name))
    for field in model._meta.many_to_many:
        setattr(field, 'verbose_name', txt(field.name))
    model._meta.app_label = StringWithTitle(app_name, txt(app_name))
    model._meta.verbose_name = txt(text)
    model._meta.verbose_name_plural = txt(text + 's')
    return model


class StringWithTitle(str):
    def __new__(cls, value, title):
        instance = str.__new__(cls, value)
        instance._title = title
        return instance

    def title(self):
        return self._title.title()

    def __copy__(self):
        return self

    def __deepcopy__(self, memodict):
        return self


def verbose_names_inline(*args):
    def model_changer(model, field_to_remove='patient'):
        if model.fieldsets:
            tuple_of_tuples = model.fieldsets[0][1]['fields']
            list_of_lists = list(list(x) for x in tuple_of_tuples)
            if field_to_remove in list_of_lists[0]:
                list_of_lists[0].remove(field_to_remove)
            model.fieldsets[0][1]['fields'] = tuple(tuple(x) for x in list_of_lists)
        return model

    def wrappee(model, field_to_remove='patient'):
        return model_changer(model, field_to_remove)

    if inspect.isclass(args[0]):
        return wrappee(args[0])

    def wrappee_with_args(model):
        return model_changer(model, args[0])

    return wrappee_with_args


def verbose_name_app(s):
    def _verbose(string):
        return force_text(string).capitalize()

    verbose = lazy(_verbose, six.text_type)
    return verbose(gettext_lazy(s))
