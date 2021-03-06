from django.db import models


class StudyRoom(models.Model):
    name = models.CharField(max_length=45)
    teacher = models.OneToOneField(
        'time_table.Teacher',
        on_delete=models.SET_NULL,
        null=True,
    )
