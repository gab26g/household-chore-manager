# Household Chore Manager

A Django application for managing shared household chores. Household members can create recurring chores, assign or claim them, rotate responsibility, track overdue work, and review completion history.

## Project status

This project is being developed for Homework 1 of the AI Dev Tools Zoomcamp 2026.

## Project plan

See [`_docs/plan.md`](_docs/plan.md) for the agreed scope, user flows, and acceptance criteria.

## Configuration

The repository does not contain a private Django secret. Local development uses
an explicitly non-secret fallback. Before deployment, set a private value through
the `DJANGO_SECRET_KEY` environment variable:

```powershell
$env:DJANGO_SECRET_KEY = "replace-with-a-long-random-value"
```
