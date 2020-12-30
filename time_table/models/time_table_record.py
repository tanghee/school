from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeTableRecord(models.Model):
    class DayOfWeek(models.TextChoices):
        MON = 'MON', _('MON')
        TUE = 'TUE', _('TUE')
        WED = 'WED', _('WED')
        THU = 'THU', _('THU')
        FRI = 'FRI', _('FRI')

    day_of_week = models.CharField(
        max_length=45,
        choices=DayOfWeek.choices,
        default=DayOfWeek.MON
    )
    period = models.IntegerField()
    time_table = models.OneToOneField(
        'time_table.TimeTable',
        on_delete=models.SET_NULL,
        null=True,
    )
