class Wspolnota(models.Model):
    nazwa = models.CharField(max_length = 255, blank = True, null = True)
    adres = models.TextField()


class Lokal(models.Model):
    wspolnota = models.ForeignKey(Wspolnota)
    numer = models.CharField(max_length = 64, blank = True, null = True)


class Udzial(models.Model):
    pass


class Czlonek(models.Model):
    pass


class Uchwala(models.Model):
    pass


class Glos(models.Model):
    pass


class DraftUchwaly(models.Model):
    pass


class Komentarz(models.Model):
    pass

