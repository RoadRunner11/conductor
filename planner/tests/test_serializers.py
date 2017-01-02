from conductor.tests import TestCase
from planner import serializers


class TestSchoolSerializer(TestCase):

    def test_serializes_id(self):
        school = self.SchoolFactory.create()
        serializer = serializers.SchoolSerializer(school)
        self.assertEqual(school.id, serializer.data['id'])

    def test_serializes_name(self):
        school = self.SchoolFactory.build(name='Johns Hopkins University')
        serializer = serializers.SchoolSerializer(school)
        self.assertEqual('Johns Hopkins University', serializer.data['name'])


class TestSemesterSerializer(TestCase):

    def test_serializes_id(self):
        semester = self.SemesterFactory.create()
        serializer = serializers.SemesterSerializer(semester)
        self.assertEqual(semester.id, serializer.data['id'])

    def test_serializes_date(self):
        semester = self.SemesterFactory.create()
        serializer = serializers.SemesterSerializer(semester)
        self.assertEqual(str(semester.date), serializer.data['date'])


class TestStudentSerializer(TestCase):

    def test_serializes_id(self):
        student = self.StudentFactory.create()
        serializer = serializers.StudentSerializer(student)
        self.assertEqual(student.id, serializer.data['id'])

    def test_serializes_first_name(self):
        student = self.StudentFactory.create()
        serializer = serializers.StudentSerializer(student)
        self.assertEqual(student.first_name, serializer.data['first_name'])

    def test_serializes_last_name(self):
        student = self.StudentFactory.create()
        serializer = serializers.StudentSerializer(student)
        self.assertEqual(student.last_name, serializer.data['last_name'])

    def test_serializes_matriculation_semester(self):
        student = self.StudentFactory.create()
        serializer = serializers.StudentSerializer(student)
        self.assertEqual(
            student.matriculation_semester.id,
            int(serializer.data['matriculation_semester']['id']))

    def test_serializes_schools(self):
        school = self.SchoolFactory.create()
        student = self.StudentFactory.create(schools=(school,))
        serializer = serializers.StudentSerializer(student)
        self.assertEqual(
            school.id,
            int(serializer.data['schools'][0]['id']))
