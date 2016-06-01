from common.models import *


class Wspolnota(models.Model):
    nazwa = models.CharField(max_length=255, blank=True, null=True)
    adres = models.TextField()


class Wlasciciel(models.Model):
    wspolnota = models.ForeignKey(Wspolnota, blank=True, null=True)
    nazwa = models.CharField(max_length=255, blank=True, null=True)
    numer = models.CharField(max_length=64, blank=True, null=True)


class Uchwala(models.Model):
    wspolnota = models.ForeignKey(Wspolnota, blank=True, null=True)
    numer = models.CharField(max_length=64, blank=True, null=True)
    tresc = models.TextField(blank=True, null=True)
    zakonczenie_glosowania = models.DateTimeField(blank=True, null=True)


class Glos(models.Model):
    uchwala = models.ForeignKey(Uchwala, blank=True, null=True)
    wlasciciel = models.ForeignKey(Uchwala, blank=True, null=True)
    oddany_glos = models.BooleanField(blank=True, null=True)


class DraftUchwaly(models.Model):
    wspolnota = models.ForeignKey(Wspolnota, blank=True, null=True)
    tresc = models.TextField(blank=True, null=True)


class Komentarz(models.Model):
    pass

