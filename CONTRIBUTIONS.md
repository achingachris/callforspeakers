# Contributions Guide

Thanks for your interest in improving CFP Explorer. This guide outlines how to propose changes smoothly.

## Getting Started
- Fork the repository and clone your fork locally: `git clone git@github.com:<you>/fastapi.git`.
- Create a virtual environment: `python -m venv .venv && source .venv/bin/activate` (PowerShell: `.\.venv\Scripts\Activate.ps1`).
- Install dependencies: `pip install --upgrade pip && pip install -r requirements.txt`.
- Keep the upstream repository configured: `git remote add upstream git@github.com:<owner>/fastapi.git`.

## Branching and Commits
- Use topic branches: `feature/<short-name>` or `fix/<short-name>`.
- Write concise, imperative commit messages (e.g., "Add draft submissions view").
- Rebase on `main` before opening a PR to keep history clean.

## Coding Standards
- Follow PEP 8 with 4-space indentation and add type hints where practical.
- Reuse existing FastAPI/HTMX patterns; keep template naming lowercase and descriptive.
- Preserve `cfp.json` structure and field names; ensure valid JSON and consistent ordering.
- Avoid committing virtualenv or environment-specific files (`bin/`, `.venv/`, `pyvenv.cfg`).

## Testing
- If you add tests, place them under `tests/` using `test_*.py` naming.
- Run relevant checks before proposing changes: manual UI (`/`, search, `/submit`, `/drafts`), and `pytest` when tests exist.
- For data changes, sanity-check `/api/events` returns valid JSON.

## Pull Requests
- Provide a clear summary of changes and why they’re needed.
- List testing performed (manual steps or `pytest` runs) and include screenshots/GIFs for UI updates.
- Call out any updates to `cfp.json` or `.vercel/` and their impact.
- Keep PRs focused; prefer smaller, reviewable changes over large bundles.

## Reporting Issues
- Use the GitHub issue templates when possible.
- Include reproduction steps, expected vs. actual behavior, environment details, and any logs or screenshots.

## Code of Conduct
- Be respectful, collaborative, and generous with feedback. Assume positive intent and keep discussions constructive.
