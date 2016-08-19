from rest_framework.test import force_authenticate

from conductor.tests import TestCase
from planner import views


class TestSchoolViewSet(TestCase):

    def test_no_create(self):
        """Sanity check that no create method is available."""
        viewset = views.SchoolViewSet()
        self.assertRaises(AttributeError, lambda: viewset.create)


class TestStudentViewSet(TestCase):

    def _make_view(self):
        return views.StudentViewSet.as_view(
            actions={'get': 'list', 'post': 'create'})

    def test_gets_students(self):
        student = self.StudentFactory.create()
        self.assertIn(student, views.StudentViewSet.queryset)

    def test_list(self):
        view = self._make_view()
        request = self.request_factory.get()
        response = view(request)
        self.assertEqual(200, response.status_code)

    def test_associates_user(self):
        view = self._make_view()
        data = {
            'first_name': 'Matt',
            'last_name': 'Layman',
            'class_year': 2002
        }
        request = self.request_factory.post(data=data)
        user = self.UserFactory.create()
        force_authenticate(request, user)
        response = view(request)
        self.assertEqual(201, response.status_code)
