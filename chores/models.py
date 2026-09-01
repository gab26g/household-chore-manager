from django.db import models


class HouseholdMember(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Chore(models.Model):
    class Recurrence(models.TextChoices):
        DAILY = "daily", "Daily"
        WEEKLY = "weekly", "Weekly"

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    recurrence = models.CharField(max_length=10, choices=Recurrence.choices)
    due_date = models.DateField()
    assignee = models.ForeignKey(
        HouseholdMember,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_chores",
    )

    class Meta:
        ordering = ["due_date", "name"]

    def __str__(self):
        return self.name


class CompletionRecord(models.Model):
    chore = models.ForeignKey(
        Chore,
        on_delete=models.CASCADE,
        related_name="completion_records",
    )
    completed_by = models.ForeignKey(
        HouseholdMember,
        on_delete=models.CASCADE,
        related_name="completion_records",
    )
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-completed_at"]

    def __str__(self):
        return f"{self.chore} completed by {self.completed_by}"
