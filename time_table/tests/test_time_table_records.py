from django.test import TestCase

from time_table.models import TimeTableRecord
from time_table.tests.test_subjects import create_subjects, create_subject


def create_time_table_record():
    day_of_week = TimeTableRecord.DayOfWeek.choices[0][0]
    time_table_record = TimeTableRecord.objects.create(day_of_week=day_of_week, period=1)
    return time_table_record


def create_time_table_records(time_table=None, subject=None):
    time_table_records = []
    day_of_week_choices = TimeTableRecord.DayOfWeek.choices
    day_of_week_names = [choice[1] for choice in day_of_week_choices]
    for day_of_week in day_of_week_names:
        for period in range(1, 3):
            time_table_record = TimeTableRecord(
                day_of_week=day_of_week,
                period=period,
                subject=subject,
                time_table=time_table,
            )
            time_table_records.append(time_table_record)
    TimeTableRecord.objects.bulk_create(time_table_records)


class TestTimeTableRecords(TestCase):
    def test_create_time_table_record(self):
        time_table_record = create_time_table_record()
        self.assertIsNotNone(time_table_record)

    def test_create_time_table_records(self):
        create_time_table_records()
        time_table_records = TimeTableRecord.objects.all()
        for time_table_record in time_table_records:
            create_subjects(time_table_record)
