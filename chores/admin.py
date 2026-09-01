from django.contrib import admin

from .models import Chore, CompletionRecord, HouseholdMember


@admin.register(HouseholdMember)
class HouseholdMemberAdmin(admin.ModelAdmin):
    search_fields = ["name"]


@admin.register(Chore)
class ChoreAdmin(admin.ModelAdmin):
    list_display = ["name", "recurrence", "due_date", "assignee"]
    list_filter = ["recurrence", "due_date"]
    search_fields = ["name", "description"]


@admin.register(CompletionRecord)
class CompletionRecordAdmin(admin.ModelAdmin):
    list_display = ["chore", "completed_by", "completed_at"]
    list_filter = ["completed_at"]
