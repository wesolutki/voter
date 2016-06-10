from django.contrib import admin
from voter.models import SzkicUchwaly, Glos, Komentarz, Uchwala, Czlonek, Wspolnota


class SzkicUchwalyAdmin(admin.ModelAdmin):
    pass
admin.site.register(SzkicUchwaly, SzkicUchwalyAdmin)


class GlosAdmin(admin.ModelAdmin):
    pass
admin.site.register(Glos, GlosAdmin)


class KomentarzAdmin(admin.ModelAdmin):
    pass
admin.site.register(Komentarz, KomentarzAdmin)


class UchwalaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Uchwala, UchwalaAdmin)


class CzlonekAdmin(admin.ModelAdmin):
    pass
admin.site.register(Czlonek, CzlonekAdmin)


class WspolnotaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Wspolnota, WspolnotaAdmin)
