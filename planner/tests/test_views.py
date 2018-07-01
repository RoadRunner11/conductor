from unittest import mock

from django.http import Http404
from django.urls import reverse

from conductor.tests import TestCase
from planner import views


class TestSchoolDetail(TestCase):

    def test_unauthenticated(self):
        school = self.SchoolFactory.create()
        request = self.request_factory.get()

        response = views.school_detail(request, school.slug)

        self.assertEqual(200, response.status_code)

    def test_bad_school(self):
        request = self.request_factory.get()

        with self.assertRaises(Http404):
            views.school_detail(request, 'bad-slug')

    @mock.patch('planner.views.render')
    def test_school_in_context(self, render):
        school = self.SchoolFactory.create()
        request = self.request_factory.get()

        views.school_detail(request, school.slug)

        context = render.call_args[0][2]
        self.assertEqual(school, context['school'])

    @mock.patch('planner.views.render')
    def test_authenticated_teplate(self, render):
        user = self.UserFactory.create()
        school = self.SchoolFactory.create()
        request = self.request_factory.authenticated_get(user)

        views.school_detail(request, school.slug)

        template = render.call_args[0][1]
        self.assertEqual('planner/school.html', template)

    @mock.patch('planner.views.render')
    def test_unauthenticated_teplate(self, render):
        school = self.SchoolFactory.create()
        request = self.request_factory.get()

        views.school_detail(request, school.slug)

        template = render.call_args[0][1]
        self.assertEqual('planner/school_unauthenticated.html', template)


class TestAddStudent(TestCase):

    def test_requires_login(self):
        request = self.request_factory.get()

        response = views.add_student(request)

        self.assertEqual(302, response.status_code)
        self.assertIn(reverse('login'), response.get('Location'))

    def test_get(self):
        user = self.UserFactory.build()
        request = self.request_factory.authenticated_get(user)

        response = views.add_student(request)

        self.assertEqual(200, response.status_code)

    @mock.patch('planner.views.render')
    def test_has_form(self, render):
        user = self.UserFactory.build()
        request = self.request_factory.authenticated_get(user)

        views.add_student(request)

        context = render.call_args[0][2]
        self.assertIn('form', context)

    @mock.patch('planner.views.render')
    def test_app_nav(self, render):
        user = self.UserFactory.build()
        request = self.request_factory.authenticated_get(user)

        views.add_student(request)

        context = render.call_args[0][2]
        self.assertEqual('add-student', context['app_nav'])

    def test_success(self):
        semester = self.SemesterFactory.create()
        data = {
            'first_name': 'Joe',
            'last_name': 'Student',
            'matriculation_semester': str(semester.id),
        }
        user = self.UserFactory.create()
        request = self.request_factory.authenticated_post(user, data=data)

        response = views.add_student(request)

        self.assertEqual(1, user.students.count())
        student = user.students.first()
        self.assertIn(
            reverse('student-profile', args=[student.id]),
            response.get('Location'))

    @mock.patch('planner.views.render')
    def test_failure(self, render):
        data = {}
        user = self.UserFactory.create()
        request = self.request_factory.authenticated_post(user, data=data)

        views.add_student(request)

        context = render.call_args[0][2]
        self.assertFalse(context['form'].is_valid())


class TestStudentProfile(TestCase):

    def test_requires_login(self):
        request = self.request_factory.get()

        response = views.student_profile(request, 1)

        self.assertEqual(302, response.status_code)
        self.assertIn(reverse('login'), response.get('Location'))

    def test_valid(self):
        user = self.UserFactory.create()
        student = self.StudentFactory(user=user)
        request = self.request_factory.authenticated_get(user)

        response = views.student_profile(request, student.id)

        self.assertEqual(200, response.status_code)

    def test_unauthorized_user(self):
        user = self.UserFactory.create()
        student = self.StudentFactory()
        request = self.request_factory.authenticated_get(user)

        with self.assertRaises(Http404):
            views.student_profile(request, student.id)

    @mock.patch('planner.views.render')
    def test_student_in_context(self, render):
        user = self.UserFactory.create()
        student = self.StudentFactory(user=user)
        request = self.request_factory.authenticated_get(user)

        views.student_profile(request, student.id)

        context = render.call_args[0][2]
        self.assertEqual(student, context['student'])

    @mock.patch('planner.views.render')
    def test_schools_in_context(self, render):
        user = self.UserFactory.create()
        student = self.StudentFactory(user=user)
        target_school = self.TargetSchoolFactory.create(student=student)
        request = self.request_factory.authenticated_get(user)

        views.student_profile(request, student.id)

        context = render.call_args[0][2]
        self.assertEqual([target_school.school], list(context['schools']))


class TestAddSchool(TestCase):

    def test_requires_login(self):
        request = self.request_factory.get()

        response = views.add_school(request, 1)

        self.assertEqual(302, response.status_code)
        self.assertIn(reverse('login'), response.get('Location'))

    def test_valid_get(self):
        user = self.UserFactory.create()
        student = self.StudentFactory(user=user)
        request = self.request_factory.authenticated_get(user)

        response = views.add_school(request, student.id)

        self.assertEqual(200, response.status_code)

    def test_valid_post(self):
        user = self.UserFactory.create()
        student = self.StudentFactory(user=user)
        school = self.SchoolFactory.create()
        data = {
            'school': str(school.id),
        }
        request = self.request_factory.authenticated_post(user, data=data)

        response = views.add_school(request, student.id)

        self.assertEqual(302, response.status_code)
        self.assertIn(
            reverse('student-profile', args=[student.id]), response.get('Location'))

    def test_unauthorized_user(self):
        user = self.UserFactory.create()
        student = self.StudentFactory()
        request = self.request_factory.authenticated_get(user)

        with self.assertRaises(Http404):
            views.add_school(request, student.id)

    @mock.patch('planner.views.render')
    def test_student_in_context(self, render):
        user = self.UserFactory.create()
        student = self.StudentFactory(user=user)
        request = self.request_factory.authenticated_get(user)

        views.add_school(request, student.id)

        context = render.call_args[0][2]
        self.assertEqual(student, context['student'])

    @mock.patch('planner.views.render')
    def test_query_in_context(self, render):
        user = self.UserFactory.create()
        student = self.StudentFactory(user=user)
        data = {
            'q': 'University of Virginia',
        }
        request = self.request_factory.authenticated_get(user, data=data)

        views.add_school(request, student.id)

        context = render.call_args[0][2]
        self.assertEqual('University of Virginia', context['q'])

    @mock.patch('planner.views.render')
    def test_form_in_context(self, render):
        user = self.UserFactory.create()
        student = self.StudentFactory(user=user)
        request = self.request_factory.authenticated_get(user)

        views.add_school(request, student.id)

        context = render.call_args[0][2]
        self.assertIn('form', context)


class TestExportSchedule(TestCase):

    def test_requires_login(self):
        request = self.request_factory.get()

        response = views.export_schedule(request, 1)

        self.assertEqual(302, response.status_code)
        self.assertIn(reverse('login'), response.get('Location'))

    def test_unauthorized_user(self):
        user = self.UserFactory.create()
        student = self.StudentFactory()
        request = self.request_factory.authenticated_get(user)

        with self.assertRaises(Http404):
            views.export_schedule(request, student.id)

    @mock.patch('planner.views.messages')
    def test_no_google_auth(self, messages):
        user = self.UserFactory.create()
        student = self.StudentFactory(user=user)
        request = self.request_factory.authenticated_get(user)

        response = views.export_schedule(request, student.id)

        messages.add_message.assert_called_once_with(
            request, messages.INFO, mock.ANY)
        self.assertEqual(302, response.status_code)
        self.assertIn(reverse('settings'), response.get('Location'))

    @mock.patch('planner.views.messages')
    @mock.patch('planner.views.build_schedule')
    def test_trigger_task(self, build_schedule, messages):
        user = self.UserFactory.create()
        self.GoogleDriveAuthFactory.create(user=user)
        student = self.StudentFactory(user=user)
        request = self.request_factory.authenticated_get(user)

        response = views.export_schedule(request, student.id)

        build_schedule.delay.assert_called_once_with(student.id)
        messages.add_message.assert_called_once_with(
            request, messages.SUCCESS, mock.ANY)
        self.assertEqual(302, response.status_code)
        self.assertIn(
            reverse('student-profile', args=[student.id]), response.get('Location'))
