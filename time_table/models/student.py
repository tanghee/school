from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=45)
    study_room = models.ForeignKey(
        'time_table.StudyRoom',
        related_name='study_room_students',
        on_delete=models.SET_NULL,
        null=True,
    )
