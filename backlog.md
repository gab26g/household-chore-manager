# Development Backlog

This backlog turns the scope in `_docs/plan.md` into small, dependency-ordered Django tasks.

## Task 1: Create the core data model

Define Django models for `HouseholdMember`, `Chore`, and `CompletionRecord`. A chore must store its name, optional description, daily or weekly recurrence, due date, and optional assignee. A completion record must identify the chore, the member who completed it, and the completion time.

**Done when:**

- The three models and their relationships are defined.
- Model validation restricts recurrence to daily or weekly.
- Models have useful string representations.
- Initial migrations are created and apply successfully.
- The models are registered in Django admin.
- Basic model tests pass.

## Task 2: Add household member management

Create pages and forms that allow anyone in the household to list, add, edit, and delete member profiles without authentication.

**Done when:**

- Member list and form pages are accessible through named URLs.
- Valid forms create and update members.
- Deleting a member requires confirmation.
- Member-management tests pass.

## Task 3: Add chore management

Create pages and forms for listing, adding, editing, and deleting daily or weekly chores. Allow a chore to be assigned to a member or left unassigned.

**Done when:**

- Chore CRUD pages and named URLs work.
- Forms validate the recurrence and due date.
- Manual assignment and reassignment work.
- Chore-management tests pass.

## Task 4: Build the dashboard and filters

Build the main dashboard showing all chores, with the option to show chores for one member. Add filters for assignee, completion status, and recurrence schedule.

**Done when:**

- The dashboard shows all chores by default.
- Filters can be used separately or together.
- Incomplete chores past their due date display an overdue label.
- Dashboard and filtering tests pass.

## Task 5: Add chore claiming

Allow a household member to claim an unassigned chore. Prevent a member from claiming a chore that is already assigned unless it is manually reassigned through the edit flow.

**Done when:**

- An unassigned chore can be claimed by a selected member.
- An already assigned chore cannot be claimed.
- Claiming behavior is covered by tests.

## Task 6: Add completion, history, and rotation

Allow the assignee to mark a chore complete through simple self-confirmation. Record the completion and create the next occurrence, assigning it to the next household member in rotation.

**Done when:**

- Completion creates a history record with the member and timestamp.
- The activity-history page displays completion records.
- The next due date is calculated from the recurrence schedule.
- The next occurrence rotates to the next member.
- Manual reassignment remains possible afterward.
- Completion and rotation scenarios are covered by tests.

## Task 7: Verify and polish the first version

Review the complete workflow, improve navigation and presentation, and add tests for important edge cases.

**Done when:**

- Users can navigate between the dashboard, members, chores, and history.
- Empty states and validation errors are understandable.
- The Django system check and complete test suite pass.
- The README contains setup and run instructions.

