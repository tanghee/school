from django.test import TestCase

from time_table.models import Student


def create_student(study_room):
    student = Student.objects.create(name="Student1", study_room=study_room)
    return student


def create_students(start, end, study_room=None):
    students = []
    for i in range(start, end):
        student_name = 'student' + str(i)
        student = Student(
            name=student_name,
            study_room=study_room,
        )
        students.append(student)
    Student.objects.bulk_create(students)


class TestStudents(TestCase):
    def test_create_student(self):
        student = create_student()
        self.assertIsNotNone(student)

    def test_create_students(self):
        create_students(start=1, end=20)
        students = Student.objects.all()
        for student in students:
            print(student)
