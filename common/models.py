# -*- coding: utf-8 -*-
#
from django.db import models
from django.core.exceptions import ValidationError


class ShortFloatField(models.FloatField):
    pass


class ShortIntegerField(models.IntegerField):
    pass


class AdditionalNotesField(models.TextField):
    pass


class DescriptionField(models.TextField):
    pass


def validate_pesel_length(value):
    if len(value) != 11:
        raise ValidationError('PESEL musi zawierać 11 cyfr')


def validate_pesel_chars(value):
    if not value.isdigit():
        raise ValidationError('PESEL musi składać się z samych cyfr')


def validate_pesel_checksum(value):
    if not value.isdigit():
        return
    multiple_table = (1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1)
    result = 0
    for i in range(len(value)):
        result += int(value[i]) * multiple_table[i]
    if result % 10 != 0:
        raise ValidationError('Suma kontrolna się nie zgadza, zły PESEL')


class PESELField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 11
        kwargs['null'] = True
        kwargs['blank'] = True
        kwargs['validators'] = [validate_pesel_length, validate_pesel_chars, validate_pesel_checksum]
        super(PESELField, self).__init__(*args, **kwargs)
