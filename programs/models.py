from django.db import models
from django.utils.translation import gettext as _
from datetime import datetime, timezone, timedelta
import pytz

RADIOS = (
    (1, _("Radio Globo")),
    (2, _("CBN")),
    (3, _("BH"))
)

TIPOS = (
    (1, _("Politica")),
    (2, _("Futebol")),
    (3, _("Saude"))
)

# Create your models here.
class Program(models.Model):
    name = models.CharField(max_length=200)
    radio = models.IntegerField(choices=RADIOS, default=1)
    start = models.DateTimeField('start date time', default=datetime.now, blank=True)
    end = models.DateTimeField('end date time', default=datetime.now, blank=True)
    ptype = models.IntegerField(choices=TIPOS, default=1, verbose_name='Tipo de programa')

    def __str__(self):
        return self.name

    @property
    def is_live(self):
        timeZone = pytz.timezone("America/Sao_Paulo")
        return ((datetime.now(timeZone) < self.end) and (datetime.now(timeZone) > self.start))

    @property
    def radio_name(self):
        if self.radio == 1:
            return 'Radio Globo'
        if self.radio == 2:
            return 'CBN'
        return 'BH'

    @property
    def p_type_name(self):
        if self.ptype == 1:
            return 'Politica'
        if self.ptype == 2:
            return 'Futebol'
        return 'Saude'

