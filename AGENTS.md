# Repository Guidelines

## Project Structure & Module Organization
- `app.py` holds the FastAPI app definition and HTMX-friendly routes rendering Jinja templates.
- `templates/` contains Jinja2 views (`base.html`, `index.html`, `events.html`) styled with Bootstrap; copy this naming style for new fragments.
- `cfp.json` stores event metadata (`name`, `link`, `deadline`, `event_date`); keep valid JSON, preserve existing fields, and favor consistent ordering when updating entries.
- `.vercel/` contains deployment metadata; avoid modifying unless adjusting hosting.
- `requirements.txt` pins runtime deps; `bin/` and `pyvenv.cfg` come from the local virtualenv—do not commit new venv artifacts.

## Build, Test, and Development Commands
- Create/activate an environment: `python -m venv .venv && source .venv/bin/activate`.
- Install deps: `pip install -r requirements.txt`.
- Run locally with reload: `uvicorn app:app --reload` (opens at `http://127.0.0.1:8000`).
- Quick API check: `curl http://127.0.0.1:8000/api/events` to confirm JSON responses.
- If you add tests, run them with `pytest` from the repo root.

## Coding Style & Naming Conventions
- Follow PEP 8 with 4-space indentation; use type hints for new functions and parameters.
- Keep FastAPI route names descriptive and HTTP verbs aligned with their actions.
- Use lowercase, descriptive filenames for templates and static assets (e.g., `events.html`).
- When editing templates, prefer Bootstrap utility classes already in use and keep HTMX attributes (`hx-get`, `hx-target`) consistent with existing patterns.
- Document any new config/env variables in the README or inline `.env.example` files rather than hardcoding defaults.

## Testing Guidelines
- No automated suite exists yet; new tests should live under `tests/` and follow `test_*.py` naming.
- Use lightweight fixtures derived from `cfp.json` to keep checks deterministic.
- Manually verify core flows after changes: `/` renders, search filtering updates `/partial/events`, and `/api/events` returns valid JSON.

## Commit & Pull Request Guidelines
- Write concise, imperative commit messages (e.g., "Update events table rendering"); keep subjects under ~72 characters.
- For pull requests, include: a short summary, testing steps (manual or pytest), and screenshots/GIFs for UI changes.
- Call out data updates to `cfp.json` explicitly and note any impact on deployment settings if `.vercel/` changes.

## Security & Configuration Tips
- Never commit secrets; store tokens or credentials in local environment variables and reference them via FastAPI settings if added later.
- Prefer dependency updates through `requirements.txt` to keep deployments reproducible; avoid adding large binaries or venv artifacts to version control.
