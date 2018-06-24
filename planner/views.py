from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from planner.forms import AddSchoolForm, AddStudentForm
from planner.models import School


@login_required
def add_student(request):
    """Add a student to the user's set."""
    if request.method == 'POST':
        form = AddStudentForm(data=request.POST)
        if form.is_valid():
            form.save(request.user)
            return HttpResponseRedirect(reverse('dashboard'))
    else:
        form = AddStudentForm()
    context = {
        'app_nav': 'add-student',
        'form': form,
    }
    return render(request, 'planner/add_student.html', context)


@login_required
def student_profile(request, student_id):
    """Show a student's information."""
    student = get_object_or_404(
        request.user.students.select_related('matriculation_semester'),
        id=student_id)
    schools = student.schools.all().order_by('name')
    context = {
        'student': student,
        'schools': schools,
    }
    return render(request, 'planner/student_profile.html', context)


@login_required
def add_school(request, student_id):
    """Add a school to a student's list."""
    student = get_object_or_404(request.user.students, id=student_id)
    query = request.GET.get('q')

    if request.method == 'POST':
        form = AddSchoolForm(student, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse('student-profile', args=[student.id]))
    else:
        form = AddSchoolForm(student)

    schools = []
    if query:
        schools = School.objects.search(query)

    context = {
        'q': query,
        'form': form,
        'schools': schools,
        'student': student,
    }
    return render(request, 'planner/add_school.html', context)
