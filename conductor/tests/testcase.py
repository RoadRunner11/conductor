from django import test

from conductor.accounts.tests.factories import (
    GoogleDriveAuthFactory, ProfileFactory, UserFactory)
from conductor.support.tests.factories import SupportTicketFactory
from conductor.tests.request_factory import RequestFactory
from planner.tests.factories import (
    ApplicationStatusFactory, AuditFactory, MilestoneFactory, SchoolFactory,
    SemesterFactory, StudentFactory, TargetSchoolFactory)


class TestCase(test.TestCase):
    request_factory = RequestFactory()

    # accounts
    GoogleDriveAuthFactory = GoogleDriveAuthFactory
    ProfileFactory = ProfileFactory
    UserFactory = UserFactory

    # planner
    ApplicationStatusFactory = ApplicationStatusFactory
    AuditFactory = AuditFactory
    MilestoneFactory = MilestoneFactory
    SchoolFactory = SchoolFactory
    SemesterFactory = SemesterFactory
    StudentFactory = StudentFactory
    TargetSchoolFactory = TargetSchoolFactory

    # support
    SupportTicketFactory = SupportTicketFactory
