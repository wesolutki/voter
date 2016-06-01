from django.contrib import admin
from easy_select2 import select2_modelform


class AksonBaseAdmin(admin.ModelAdmin):
    actions = None

    def get_form(self, request, obj=None, **kwargs):
        form = super(AksonBaseAdmin, self).get_form(request, obj, **kwargs)
        usernames = ['therapist', 'leading_people', 'examiners', 'orderer']
        for username in usernames:
            if username in tuple(form.base_fields):
                form.base_fields[username].initial = [request.user.pk]
        return form

    def __init__(self, model, admin_site):
        self.form = select2_modelform(model, attrs={'width': '21em'})
        super(AksonBaseAdmin, self).__init__(model, admin_site)


class AksonCardAdmin(AksonBaseAdmin):
    search_fields = ['patient__last_name', 'patient__first_name']
