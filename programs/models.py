from django.db import models
from django.utils.translation import gettext as _
from datetime import datetime    

RADIOS = (
    (1, _("Radio Globo")),
    (2, _("CBN")),
    (3, _("BH"))
)

# Create your models here.
class Program(models.Model):
    name = models.CharField(max_length=200)
    radio = models.IntegerField(choices=RADIOS, default=1)
    start = models.DateTimeField('start date time', default=datetime.now, blank=True)
    end = models.DateTimeField('end date time', default=datetime.now, blank=True)

    def __str__(self):
        return self.name