from django.db import models


class TimeTable(models.Model):
    study_room = models.ForeignKey(
        'time_table.StudyRoom',
        related_name='study_room_time_tables',
        on_delete=models.SET_NULL,
        null=True,
    )
