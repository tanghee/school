from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=45)
    time_table = models.ForeignKey(
        'time_table.TimeTable',
        related_name='time_table_subjects',
        on_delete=models.SET_NULL,
        null=True,
    )
    teacher = models.ManyToManyField(
        'time_table.Teacher',
        related_name='teacher_subjects',
    )
