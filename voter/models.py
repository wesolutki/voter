from common.models import *


class Wspolnota(models.Model):
    nazwa = models.CharField(max_length=255)
    adres = models.TextField()


class Wlasciciel(models.Model):
    wspolnota = models.ForeignKey(Wspolnota)
    nazwa = models.CharField(max_length=255)
    numer = models.CharField(max_length=64)
    udzial = models.FloatField()


class Uchwala(models.Model):
    wspolnota = models.ForeignKey(Wspolnota)
    numer = models.CharField(max_length=64)
    tresc = models.TextField()
    zakonczenie_glosowania = models.DateTimeField()


class Glos(models.Model):
    uchwala = models.ForeignKey(Uchwala)
    wlasciciel = models.ForeignKey(Wlasciciel)
    decyzja = models.BooleanField()


class DraftUchwaly(models.Model):
    wspolnota = models.ForeignKey(Wspolnota)
    tresc = models.TextField()


class Komentarz(models.Model):
    pass

