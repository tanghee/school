from django.core.management.base import BaseCommand
from time_table.models import StudyRoom, Teacher, TimeTableRecord, TimeTable
from time_table.tests.test_students import create_students
from time_table.tests.test_study_rooms import create_study_rooms
from time_table.tests.test_subjects import create_subjects
from time_table.tests.test_teachers import create_teachers
from time_table.tests.test_time_table_records import create_time_table_records
from time_table.tests.test_time_tables import create_time_tables


class Command(BaseCommand):
    help = 'Create school.'

    def handle(self, *args, **options):
        create_teachers()

        study_rooms = StudyRoom.objects.all()
        student_count = 20

        for study_room in study_rooms:
            start = student_count * (study_room.id - 1) + 1
            end = student_count * study_room.id + 1
            create_students(start, end, study_room)
            create_time_tables(study_room)

        teachers = Teacher.objects.all()
        for teacher in teachers:
            create_study_rooms(teacher)

        time_table_records = TimeTableRecord.objects.all()
        for time_table_record in time_table_records:
            create_subjects(time_table_record)

        time_tables = TimeTable.objects.all()
        for time_table in time_tables:
            create_time_table_records(time_table)
