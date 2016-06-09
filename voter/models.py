from common.models import *


class Wspolnota(models.Model):
    nazwa = models.CharField(max_length=255)
    adres = models.TextField()


class Czlonek(models.Model):
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
    czlonek = models.ForeignKey(czlonek)
    decyzja = models.BooleanField(widget=RadioSelect(choices=YES_OR_NO))
    TAK_LUB_NIE = (
        (True, 'Tak'),
        (False, 'Nie')
    )



class SzkicUchwaly(models.Model):
    wspolnota = models.ForeignKey(Wspolnota)
    tresc = models.TextField()


class Komentarz(models.Model):
    pass

