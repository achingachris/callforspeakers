from pathlib import Path
import json

from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from typing import Union


app = FastAPI(title="2026 Call For Speakers Explorer")

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "cfp.json"

with DATA_PATH.open() as f:
    CFP_DATA = json.load(f)

EVENTS = CFP_DATA["events"]

templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

@app.get("/", response_class=HTMLResponse)
async def home(request: Request, q: str | None = Query(default=None)):
    if q:
        q_lower = q.lower()
        filtered_events = [e for e in EVENTS if q_lower in e["name"].lower()]
    else:
        filtered_events = EVENTS

    context = {
        "request": request,
        "year": CFP_DATA["year"],
        "title": CFP_DATA["title"],
        "events": filtered_events,
        "query": q or "",
        "total_events": len(EVENTS),
        "shown_events": len(filtered_events),
    }
    return templates.TemplateResponse("index.html", context)

@app.get("/api/events")
async def list_events():
    return {
        "year": CFP_DATA["year"],
        "title": CFP_DATA["title"],
        "events": EVENTS,
    }
    
@app.get("/api/events/search")
async def search_events(q: str):
    q_lower = q.lower()
    filtered_events = [e for e in EVENTS if q_lower in e["name"].lower()]
    return {
        "year": CFP_DATA["year"],
        "title": CFP_DATA["title"],
        "query": q,
        "events": filtered_events,
        "total": len(filtered_events),
    }
    