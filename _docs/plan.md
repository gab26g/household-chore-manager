# Shared Household Chore Manager

## Overview

A simple Django web application for one household to organize recurring chores, share responsibility, and track completed work. The first version uses household member profiles without user accounts or authentication.

## Goals

- Make it easy to see what chores need to be done and who is responsible.
- Support flexible assignment through manual assignment, self-claiming, and automatic rotation.
- Highlight overdue work without adding penalties or complex notifications.
- Preserve a simple history of completed chores for accountability.

## Core Features

### 1. Recurring chores

Household members can create, edit, and delete chores that repeat daily or weekly. Each chore includes a name, optional description, recurrence schedule, due date, and current assignee when one exists.

### 2. Flexible assignment

A chore can be assigned manually to a household member or left unassigned for someone to claim. After a recurring chore is completed, its next occurrence is assigned to the next household member in rotation. Any member can manually reassign it afterward.

### 3. Dashboard and overdue status

The dashboard can show all household chores or only chores assigned to a selected member. Members can filter chores by assignee, completion status, and schedule. An incomplete chore past its due date displays an overdue label.

### 4. Completion history

Members mark chores complete through simple self-confirmation; no approval is required. The app records the chore, the member who completed it, and the completion time in a household activity history.

## Household Rules

- The first version supports one household.
- Members use simple profiles and do not need accounts or passwords.
- Every member has equal permission to manage chores and member profiles.
- Chores recur daily or weekly; one-time and custom schedules are out of scope.

## Main User Flows

1. A member opens the dashboard and views all chores or filters the list.
2. A member creates a daily or weekly chore and assigns it or leaves it available to claim.
3. A member claims an unassigned chore or manually reassigns a chore.
4. The assignee marks a chore complete.
5. The app records the completion and creates the next occurrence with the next member in rotation.
6. A member reviews the household activity history.

## Acceptance Criteria

- Members can be created, edited, and deleted.
- Daily and weekly chores can be created, edited, and deleted.
- Chores can be manually assigned, reassigned, or claimed when unassigned.
- Completing a recurring chore records an activity-history entry.
- The next occurrence rotates to the next household member.
- Incomplete chores past their due date are visibly marked overdue.
- The dashboard supports all-household and per-member views.
- Chores can be filtered by assignee, completion status, and schedule.

## Out of Scope

- Authentication, invitations, and multiple households
- Approval of completed chores
- Points, rewards, penalties, or leaderboards
- Email, push, or in-app notifications
- One-time chores and fully custom recurrence schedules
- Different permission levels or administrator roles

