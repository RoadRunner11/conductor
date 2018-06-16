from django import forms

from planner.models import School, Semester, Student, TargetSchool


class AddSchoolForm(forms.Form):
    school = forms.IntegerField()

    def __init__(self, student, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.student = student

    def clean_school(self):
        """Check that the student does not already have the selected school."""
        school_id = self.cleaned_data.get('school')
        school = School.objects.get(id=school_id)
        if TargetSchool.objects.filter(
                student=self.student, school=school).exists():
            raise forms.ValidationError(
                '{} is already on the student’s list.'.format(school.name))
        return school

    def save(self):
        """Create a target school for the student."""
        TargetSchool.objects.create(
            student=self.student, school=self.cleaned_data['school'])


class AddStudentForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    matriculation_semester = forms.ModelChoiceField(
        label='Applying for',
        queryset=Semester.objects.filter(active=True),
        empty_label=None)

    def save(self, user):
        """Create a new student."""
        Student.objects.create(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            matriculation_semester=self.cleaned_data['matriculation_semester'],
            user=user)
