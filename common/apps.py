import os
from common.localization import verbose_name_app
from django.apps import AppConfig


def app_name(filename):
    return os.path.basename(os.path.normpath(os.path.dirname(os.path.realpath(filename))))


def common_app_config(filename):
    def wrap(f):
        class CommonAppConfig(AppConfig):
            name = app_name(filename)
            verbose_name = verbose_name_app(name)
        return CommonAppConfig
    return wrap


def default_app_config_string(filename):
    return '.'.join([app_name(filename), 'AppConfig'])
