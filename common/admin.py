from django.contrib import admin
from easy_select2 import select2_modelform


class VoterBaseAdmin(admin.ModelAdmin):
    actions = None

    def __init__(self, model, admin_site):
        self.form = select2_modelform(model, attrs={'width': '21em'})
        super(VoterBaseAdmin, self).__init__(model, admin_site)


class VoterCardAdmin(VoterBaseAdmin):
    search_fields = ['patient__last_name', 'patient__first_name']
