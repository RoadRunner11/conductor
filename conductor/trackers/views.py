from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from conductor.core.decorators import staff_required
from conductor.planner.models import School
from conductor.trackers.models import CommonAppTracker


COMMON_WORDS = ("university", "college", "of", "the", "a")


@staff_required
def connect_common_apps(request: HttpRequest) -> HttpResponse:
    """A tool to connect CommonAppTrackers to Schools."""
    if request.method == "POST":
        common_app_tracker_id = request.POST.get("common_app_tracker")
        school_id = request.POST.get("school")
        common_app_tracker = CommonAppTracker.objects.get(id=common_app_tracker_id)
        common_app_tracker.school_id = school_id
        common_app_tracker.status = CommonAppTracker.TRACKED
        common_app_tracker.save()
        return HttpResponseRedirect(reverse("trackers:connect-common-apps"))

    common_app_tracker = CommonAppTracker.objects.filter(
        status=CommonAppTracker.PENDING
    ).first()

    schools = []
    if common_app_tracker:
        school_name_parts = common_app_tracker.name.split()
        for school_name_part in school_name_parts:
            if school_name_part.lower() in COMMON_WORDS:
                continue
            schools.extend(
                list(School.objects.filter(name__icontains=school_name_part))
            )

    context: dict = {"common_app_tracker": common_app_tracker, "schools": schools}
    return render(request, "trackers/connect_common_apps.html", context)
