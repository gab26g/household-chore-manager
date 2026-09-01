from datetime import date

from django.contrib import admin
from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import Chore, CompletionRecord, HouseholdMember


class HouseholdMemberModelTests(TestCase):
    def test_string_representation_is_member_name(self):
        member = HouseholdMember.objects.create(name="Alex")

        self.assertEqual(str(member), "Alex")


class ChoreModelTests(TestCase):
    def setUp(self):
        self.member = HouseholdMember.objects.create(name="Alex")

    def test_chore_stores_core_fields(self):
        chore = Chore.objects.create(
            name="Wash dishes",
            description="Clean and put away the dishes.",
            recurrence=Chore.Recurrence.DAILY,
            due_date=date(2026, 9, 2),
            assignee=self.member,
        )

        self.assertEqual(str(chore), "Wash dishes")
        self.assertEqual(chore.assignee, self.member)
        self.assertEqual(chore.recurrence, Chore.Recurrence.DAILY)

    def test_assignee_is_optional(self):
        chore = Chore.objects.create(
            name="Take out trash",
            recurrence=Chore.Recurrence.WEEKLY,
            due_date=date(2026, 9, 7),
        )

        self.assertIsNone(chore.assignee)

    def test_recurrence_rejects_unsupported_value(self):
        chore = Chore(
            name="Wash windows",
            recurrence="monthly",
            due_date=date(2026, 9, 30),
        )

        with self.assertRaises(ValidationError):
            chore.full_clean()


class CompletionRecordModelTests(TestCase):
    def test_record_identifies_chore_member_and_time(self):
        member = HouseholdMember.objects.create(name="Sam")
        chore = Chore.objects.create(
            name="Vacuum",
            recurrence=Chore.Recurrence.WEEKLY,
            due_date=date(2026, 9, 6),
            assignee=member,
        )

        record = CompletionRecord.objects.create(
            chore=chore,
            completed_by=member,
        )

        self.assertEqual(record.chore, chore)
        self.assertEqual(record.completed_by, member)
        self.assertIsNotNone(record.completed_at)
        self.assertEqual(str(record), "Vacuum completed by Sam")


class AdminRegistrationTests(TestCase):
    def test_core_models_are_registered(self):
        self.assertIn(HouseholdMember, admin.site._registry)
        self.assertIn(Chore, admin.site._registry)
        self.assertIn(CompletionRecord, admin.site._registry)
