from django.db import models
from copy import deepcopy
from common.admin import AksonBaseAdmin, admin
from common.localization import verbose_names_inline
from auth.models import Patient


class PatientCardAdmin(AksonBaseAdmin):
    change_form_template = 'patient.html'
    model = Patient
    fieldsets = (
        (('Private'),
         {'fields': (
             ('first_name', 'last_name'),
             ('gender', 'blood_type'),
             ('pesel', 'birth_date'),
         )}),
        (('Address data'),
         {'fields': (('country', 'city', 'address'),
                     )}),
        (('Mailing address'),
         {'fields': (('mailing_country', 'mailing_city', 'mailing_address'),
                     )}),
        (('Work'),
         {'fields': (('job', 'workplace'),
                     )}),
        (('Contact'),
         {'fields': (('cell_phone', 'landline_phone', 'email'),
                     )}),
        (('Injury info'),
         {'fields': (('date_of_injury', 'time_of_injury',),
                     ('date_of_operation', 'time_of_operation',),
                     ('additional_notes',)
                     )})
    )

    # TODO ogarnac, bo duzo sqlowych zapytan robi
    def levels_of_injury(self, obj):
        timespreads = obj.timespread_set.order_by('-begin')
        if len(timespreads) > 0:
            levels_of_injurys = timespreads[0].levels_of_injury.all()
            if len(levels_of_injurys) > 0:
                return ', '.join([injury.name for injury in levels_of_injurys])
        return ('None')
    levels_of_injury.short_description = ('levels_of_injury')

    def asia(self, obj):
        timespreads = obj.timespread_set.order_by('-begin')
        if len(timespreads) > 0:
            asias = timespreads[0].asia.all()
            if len(asias) > 0:
                return ', '.join([asia.name for asia in asias])
        return ('None')
    asia.short_description = ('asia')

    list_display = ('last_name', 'first_name', 'birth_date', 'date_of_injury', 'levels_of_injury', 'asia')
    search_fields = ['last_name', 'first_name']

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        return super(PatientCardAdmin, self).change_view(request, object_id=object_id, form_url=form_url,
                                                         extra_context=extra_context)

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Patient, PatientCardAdmin)

