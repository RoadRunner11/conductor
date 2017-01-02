from rest_framework_json_api import serializers

from planner.models import School, Semester, Student


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('id', 'name')


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = ('id', 'date')


class StudentSerializer(serializers.ModelSerializer):
    included_serializers = {
        'matriculation_semester': SemesterSerializer,
    }

    class Meta:
        model = Student
        fields = (
            'id',
            'first_name',
            'last_name',
            'matriculation_semester',
            'schools',
        )

    class JSONAPIMeta:
        # XXX: Side loading is currently broken in DJA.
        # See https://github.com/django-json-api/django-rest-framework-json-api/issues/291
        included_resources = ['matriculation_semester']
