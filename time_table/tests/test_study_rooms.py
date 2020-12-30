from django.test import TestCase

from time_table.models import StudyRoom
from time_table.tests.test_students import create_students
from time_table.tests.test_time_tables import create_time_tables


def create_study_room(teacher):
    study_room = StudyRoom.objects.create(name="1반", teacher=teacher)
    return study_room


def create_study_rooms(teacher=None):
    study_rooms = []
    for i in range(1, 3):
        study_room_name = str(i) + '반'
        study_room = StudyRoom(
            name=study_room_name,
            teacher=teacher,
        )
        study_rooms.append(study_room)

    StudyRoom.objects.bulk_create(study_rooms)


class TestStudyRooms(TestCase):
    def test_create_study_room(self):
        study_room = create_study_room()
        self.assertIsNotNone(study_room)

    def test_create_study_rooms(self):
        create_study_rooms()
        study_rooms = StudyRoom.objects.all()
        for study_room in study_rooms:
            print(study_room)

    def test_create_student_and_time_table_with_study_rooms(self):
        create_study_rooms()
        study_rooms = StudyRoom.objects.all()
        student_count = 20

        for study_room in study_rooms:
            start = student_count * (study_room.id - 1) + 1
            end = student_count * study_room.id + 1
            create_students(start, end, study_room)
            create_time_tables(study_room)
