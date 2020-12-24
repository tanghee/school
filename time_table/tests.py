from django.test import TestCase

from time_table.models import Student
from time_table.models import StudyRoom


class TestStudents(TestCase):
    def create_students(self):
        students = []
        for i in range(50):
            student_name = 'student' + str(i)

        student = Student(
            name=student_name,
        )
        students.append(student)
    Student.objects.bulk_create(students)

    def create_study_rooms(self):
        study_rooms = []
        for i in range(2):
            study_room_name = str(i) + '반'

        study_room = StudyRoom(
            name=study_room_name,
        )
        students.append(study_room)
    Student.objects.bulk_create(study_rooms)

    def test_create_student(self):
        self.create_students()
        students = Student.objects.all()
        for student in students:
            print(student)

    def test_create_study_room(self):
        self.create_study_rooms()
        study_rooms = StudyRoom.objects.all()
        for study_room in study_rooms:
            print(study_room)

