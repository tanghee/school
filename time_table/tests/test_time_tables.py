from django.test import TestCase

from time_table.models import TimeTable
from time_table.tests.test_time_table_records import create_time_table_records


def create_time_table():
    time_table = TimeTable.objects.create()
    return time_table


def create_time_tables(study_room=None):
    time_tables = []
    time_table = TimeTable(
        study_room=study_room,
    )
    time_tables.append(time_table)
    TimeTable.objects.bulk_create(time_tables)


class TestTimeTables(TestCase):
    def test_create_time_table(self):
        time_table = create_time_table()
        self.assertIsNotNone(time_table)

    def test_create_time_tables(self):
        create_time_tables()
        time_tables = TimeTable.objects.all()
        for time_table in time_tables:
            create_time_table_records(time_table)
