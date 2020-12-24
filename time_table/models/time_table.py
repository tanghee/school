from django.db import models


class TimeTable(models.Model):
    DAY_OF_WEEK_CHOICES = (
        ('MON', 'MON'),
        ('TUE', 'TUE'),
        ('WED', 'WED'),
        ('THU', 'THU'),
        ('FRI', 'FRI'),
    )
    period = models.IntegerField()
    day_of_week = models.CharField(max_length=45, choices=DAY_OF_WEEK_CHOICES)
