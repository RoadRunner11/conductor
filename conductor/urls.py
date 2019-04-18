import os

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from conductor.accounts.views import (
    authorize_google,
    dashboard,
    deactivate,
    index,
    oauth2_callback,
    signup,
    user_settings,
)
from conductor.support.views import contact, tools_dashboard
from conductor.planner.views import (
    add_school,
    add_student,
    export_schedule,
    remove_school,
    school_detail,
    set_student_milestone,
    set_student_school_application,
    student_profile,
)

urlpatterns = [
    # Marketing/non-authenticated views
    path("", index, name="index"),
    path("signup/", signup, name="signup"),
    path("contact/", contact, name="contact"),
    path("support/tools/", tools_dashboard, name="tools-dashboard"),
    path("terms/", TemplateView.as_view(template_name="terms.html"), name="terms"),
    path(
        "privacy/", TemplateView.as_view(template_name="privacy.html"), name="privacy"
    ),
    path(
        "sitemap.xml",
        TemplateView.as_view(template_name="sitemap.xml", content_type="text/xml"),
        name="sitemap",
    ),
    path(
        "deactivated/",
        TemplateView.as_view(template_name="accounts/deactivated.html"),
        name="deactivated",
    ),
    # Authenticated views
    path("app/", dashboard, name="dashboard"),
    path("settings/", user_settings, name="settings"),
    path("authorize-google/", authorize_google, name="authorize-google"),
    path("oauth2/", oauth2_callback, name="oauth2"),
    path("deactivate/", deactivate, name="deactivate"),
    path("schools/<slug:slug>/", school_detail, name="school-detail"),
    # Students
    path("students/add/", add_student, name="add-student"),
    path("students/<int:student_id>/", student_profile, name="student-profile"),
    path("students/<int:student_id>/add-school/", add_school, name="add-school"),
    path(
        "students/<int:student_id>/remove-school/", remove_school, name="remove-school"
    ),
    path("students/<int:student_id>/export/", export_schedule, name="export-schedule"),
    path(
        "students/<int:student_id>/milestones/",
        set_student_milestone,
        name="set-student-milestone",
    ),
    path(
        "students/<int:student_id>/school-applications/",
        set_student_school_application,
        name="set-student-school-application",
    ),
    path("accounts/", include("django.contrib.auth.urls")),
    path("admin/", admin.site.urls),
    path("trackers/", include("conductor.trackers.urls")),
]

if os.environ["DJANGO_SETTINGS_MODULE"] == "settings.development":
    import debug_toolbar
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # Make it possible to see the custom error pages.
    urlpatterns += [
        path("404/", TemplateView.as_view(template_name="404.html")),
        path("500/", TemplateView.as_view(template_name="500.html")),
    ]
