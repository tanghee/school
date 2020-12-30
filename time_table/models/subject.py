from django.db import models
from django.utils.translation import gettext_lazy as _


class Subject(models.Model):
    class Name(models.TextChoices):
        JAVA = 'JAVA', _('JAVA')
        PYTHON = 'PYTHON', _('PYTHON')
        C = 'C', _('C')
        DJANGO = 'DJANGO', _('DJANGO')

    name = models.CharField(
        max_length=45,
        choices=Name.choices,
        default=Name.JAVA,
    )
    teachers = models.ManyToManyField(
        'time_table.Teacher',
        related_name='teacher_subjects',
    )
    time_table_record = models.ForeignKey(
        'time_table.TimeTableRecord',
        related_name='time_table_record_subjects',
        on_delete=models.SET_NULL,
        null=True,
    )
