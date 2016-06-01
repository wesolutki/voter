from django.db.models.base import ModelBase
from django.core.urlresolvers import reverse, NoReverseMatch
from django.contrib import admin
from django.contrib.auth.models import User


# noinspection PyProtectedMember
def adminviews_test(self):
    password = 'test'
    user = User.objects.create_superuser('test', 'test@test.com', password)
    self.client.login(username=user.username, password=password)
    pkg = self.__module__.rpartition('.')[0]
    if pkg.endswith(".tests"):
        pkg = pkg[:-6]
    models_mod = __import__(pkg + ".models")
    if not getattr(models_mod, "models", None):
        return
    for id_ in dir(models_mod.models):
        model = getattr(models_mod.models, id_)
        if isinstance(model, ModelBase) and model._meta.app_label == pkg and model in admin.site._registry:
            # noinspection PyProtectedMember
            def check_url(sufix):
                url = reverse("admin:%s_%s_%s" % (model._meta.app_label, model._meta.model_name, sufix))
                response = self.client.get(url, follow=True)
                self.failUnlessEqual(response.status_code, 200,
                                     "%s != %s -> %s, url: %s" % (response.status_code, 200, repr(model), url))
                self.assertFalse("this_is_the_login_form" in repr(response.content),
                                 "login requested for %s" % repr(model))

            try:
                # Prevent error 405 if model_admin.has_add_permission always return False
                if admin.site._registry[model].has_add_permission(type("request", (), {"user": user})):
                    check_url('add')
                check_url('changelist')
            except NoReverseMatch:
                continue
