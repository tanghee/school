from django.test import TestCase

from time_table.models import Teacher
from time_table.tests.test_study_rooms import create_study_rooms


def create_teacher():
    teacher = Teacher.objects.create(name="teacher1")
    return teacher


def create_teachers():
    teachers = []
    for i in range(1, 11):
        teacher_name = 'teacher' + str(i)
        teacher = Teacher(
            name=teacher_name,
        )
        teachers.append(teacher)
    Teacher.objects.bulk_create(teachers)


class TestTeachers(TestCase):
    def test_create_teacher(self):
        teacher = create_teacher()
        self.assertIsNotNone(teacher)

    def test_create_teachers(self):
        create_teachers()
        teachers = Teacher.objects.all()
        for teacher in teachers:
            create_study_rooms(teacher)
