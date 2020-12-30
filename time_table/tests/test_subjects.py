from django.test import TestCase

from time_table.models import Subject


def create_subject(teacher):
    name = Subject.Name.choices[0][0]
    subject = Subject.objects.create(teacher=teacher, name=name)
    return subject


def create_subjects(teachers=None, time_table_record=None):
    subjects = []
    subject_choices = Subject.Name.choices
    subject_names = [choice[0] for choice in subject_choices]
    for name in subject_names:
        subject = Subject(
            name=name,
            time_table_record=time_table_record,
        )
        if teachers:
            subject.teachers.add(*teachers)
        subjects.append(subject)
    Subject.objects.bulk_create(subjects)


class TestSubjects(TestCase):
    def test_create_subject(self):
        subject = create_subject()
        self.assertIsNotNone(subject)

    def test_create_subjects(self):
        create_subjects()
        subjects = Subject.objects.all()
        for subject in subjects:
            print(subject)
