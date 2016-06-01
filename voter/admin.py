from django.contrib import admin
from voter.models import DraftUchwaly, Glos, Komentarz, Uchwala, Wlasciciel, Wspolnota


class DraftUchwalyAdmin(admin.ModelAdmin):
    pass
admin.site.register(DraftUchwaly, DraftUchwalyAdmin)


class GlosAdmin(admin.ModelAdmin):
    pass
admin.site.register(Glos, GlosAdmin)


class KomentarzAdmin(admin.ModelAdmin):
    pass
admin.site.register(Komentarz, KomentarzAdmin)


class UchwalaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Uchwala, UchwalaAdmin)


class WlascicielAdmin(admin.ModelAdmin):
    pass
admin.site.register(Wlasciciel, WlascicielAdmin)


class WspolnotaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Wspolnota, WspolnotaAdmin)
