from django import test

from conductor.accounts.tests.factories import (
    GoogleDriveAuthFactory,
    ProductPlanFactory,
    ProfileFactory,
    UserFactory,
)
from conductor.planner.tests.factories import (
    ApplicationScheduleFactory,
    AuditFactory,
    MilestoneFactory,
    SchoolFactory,
    SchoolApplicationFactory,
    SemesterFactory,
    StudentFactory,
    TargetSchoolFactory,
)
from conductor.support.tests.factories import SupportTicketFactory
from conductor.tests.request_factory import RequestFactory
from conductor.trackers.tests.factories import CommonAppTrackerFactory
from conductor.vendor.tests.factories import PromptSchoolFactory


class TestCase(test.TestCase):
    request_factory = RequestFactory()

    # accounts
    GoogleDriveAuthFactory = GoogleDriveAuthFactory
    ProductPlanFactory = ProductPlanFactory
    ProfileFactory = ProfileFactory
    UserFactory = UserFactory

    # planner
    ApplicationScheduleFactory = ApplicationScheduleFactory
    AuditFactory = AuditFactory
    MilestoneFactory = MilestoneFactory
    SchoolFactory = SchoolFactory
    SchoolApplicationFactory = SchoolApplicationFactory
    SemesterFactory = SemesterFactory
    StudentFactory = StudentFactory
    TargetSchoolFactory = TargetSchoolFactory

    # support
    SupportTicketFactory = SupportTicketFactory

    # trackers
    CommonAppTrackerFactory = CommonAppTrackerFactory

    # vendor
    PromptSchoolFactory = PromptSchoolFactory
