from pathlib import Path
import json

from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="CFP Explorer HTMX")

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "cfp.json"

with DATA_PATH.open() as f:
    CFP_DATA = json.load(f)

EVENTS = CFP_DATA["events"]

templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "year": CFP_DATA["year"],
        "title": CFP_DATA["title"],
        "events": EVENTS
    })


@app.get("/partial/events", response_class=HTMLResponse)
async def events_partial(request: Request, q: str | None = Query(default=None)):
    if q:
        q_lower = q.lower()
        filtered = [e for e in EVENTS if q_lower in e["name"].lower()]
    else:
        filtered = EVENTS

    return templates.TemplateResponse("events.html", {
        "request": request,
        "events": filtered
    })


@app.get("/api/events")
async def api_all():
    return CFP_DATA
