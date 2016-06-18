import datetime

from conductor.tests import TestCase


class TestMilestone(TestCase):

    def test_has_date(self):
        date = datetime.datetime.now()
        milestone = self.MilestoneFactory.build(date=date)
        self.assertEqual(date, milestone.date)


class TestSchool(TestCase):

    def test_has_name(self):
        school = self.SchoolFactory.build(name='University of Virginia')
        self.assertEqual('University of Virginia', school.name)

    def test_has_slug(self):
        school = self.SchoolFactory.build(slug='university-of-virginia')
        self.assertEqual('university-of-virginia', school.slug)

    def test_has_url(self):
        school = self.SchoolFactory.build(url='http://www.virginia.edu/')
        self.assertEqual('http://www.virginia.edu/', school.url)

    def test_has_milestones_url(self):
        school = self.SchoolFactory.build(
            milestones_url='http://admission.virginia.edu/events')
        self.assertEqual(
            'http://admission.virginia.edu/events', school.milestones_url)


class TestStudent(TestCase):

    def test_factory(self):
        student = self.StudentFactory.build()

        self.assertIsNotNone(student.user)
        self.assertNotEqual('', student.first_name)
        self.assertNotEqual('', student.last_name)
        self.assertIsNotNone(student.class_year)

    def test_has_user(self):
        user = self.UserFactory.build()
        student = self.StudentFactory.build(user=user)

        self.assertEqual(user, student.user)

    def test_has_first_name(self):
        student = self.StudentFactory.build(first_name='Matt')

        self.assertEqual('Matt', student.first_name)

    def test_has_last_name(self):
        student = self.StudentFactory.build(last_name='Layman')

        self.assertEqual('Layman', student.last_name)

    def test_has_class_year(self):
        student = self.StudentFactory.build(class_year=2002)

        self.assertEqual(2002, student.class_year)

    def test_default_class_year(self):
        today = datetime.date.today()
        student = self.StudentFactory.build()

        self.assertEqual(today.year, student.class_year)
