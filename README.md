# CFP Explorer (FastAPI + HTMX)

A lightweight Call for Proposals explorer built with FastAPI, HTMX, and Bootstrap. It renders event data from `cfp.json`, supports live filtering, and serves a simple JSON API for integrations.

## Project Structure
- `app.py` — FastAPI app, routes, and Jinja template wiring.
- `templates/` — Jinja2 views (`base.html`, `index.html`, `events.html`) styled with Bootstrap and HTMX attributes.
- `cfp.json` — Event metadata (`name`, `link`, `deadline`, `event_date`); keep fields intact and ordering consistent when editing.
- `.vercel/` — Deployment metadata for hosting; avoid changes unless adjusting deploy settings.
- `requirements.txt` — Runtime dependencies. `bin/` and `pyvenv.cfg` belong to the local virtualenv; do not commit new venv artifacts.

## Fork, Clone, and Install
1. Fork the repository on GitHub.
2. Clone your fork: `git clone git@github.com:<your-username>/fastapi.git && cd fastapi`.
3. Optional: add the original repo as upstream (`git remote add upstream git@github.com:<owner>/fastapi.git`).
4. Create a virtualenv and activate it:
   - macOS/Linux: `python -m venv .venv && source .venv/bin/activate`
   - Windows (PowerShell): `python -m venv .venv; .\.venv\Scripts\Activate.ps1`
5. Install dependencies: `pip install --upgrade pip && pip install -r requirements.txt`.

## Run the App
- Start the dev server with reload: `uvicorn app:app --reload` (default at `http://127.0.0.1:8000`).
- Quick API check: `curl http://127.0.0.1:8000/api/events` should return the CFP JSON.
- If you add tests, run them from the repo root with `pytest`.

## Contributing
- Create topic branches (`feature/<name>` or `fix/<name>`) rather than committing to `main`.
- Commit messages should be concise and imperative (e.g., "Update events table rendering").
- For pull requests, include a summary, testing steps (manual or `pytest`), and screenshots/GIFs for UI changes.
- When updating `cfp.json`, double-check JSON validity and note data changes in the PR description; avoid committing virtualenv files.
- Follow PEP 8 (4-space indentation) and reuse existing naming and HTMX patterns in templates.
