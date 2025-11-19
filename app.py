from pathlib import Path
import json
from uuid import uuid4

from fastapi import FastAPI, Request, Query, Form, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="CFP Explorer HTMX")

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "cfp.json"
DRAFTS_PATH = BASE_DIR / "drafts.json"

with DATA_PATH.open() as f:
    CFP_DATA = json.load(f)

EVENTS = CFP_DATA["events"]


def load_drafts() -> list[dict]:
    if DRAFTS_PATH.exists():
        with DRAFTS_PATH.open() as f:
            data = json.load(f)
            return data.get("drafts", [])
    return []


def save_drafts(drafts: list[dict]) -> None:
    with DRAFTS_PATH.open("w") as f:
        json.dump({"drafts": drafts}, f, indent=2)


def save_events() -> None:
    with DATA_PATH.open("w") as f:
        json.dump(CFP_DATA, f, indent=2)


DRAFTS = load_drafts()

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


@app.get("/submit", response_class=HTMLResponse)
async def submit_form(request: Request):
    return templates.TemplateResponse("submit.html", {
        "request": request,
        "year": CFP_DATA["year"],
        "title": CFP_DATA["title"]
    })


@app.post("/submit")
async def submit_event(
    name: str = Form(...),
    link: str = Form(...),
    deadline: str | None = Form(default=None),
    event_date: str | None = Form(default=None)
):
    draft = {
        "id": str(uuid4()),
        "name": name,
        "link": link,
        "deadline": deadline or None,
        "event_date": event_date or None,
        "status": "draft"
    }
    DRAFTS.append(draft)
    save_drafts(DRAFTS)
    return RedirectResponse(url="/drafts", status_code=status.HTTP_302_FOUND)


@app.get("/drafts", response_class=HTMLResponse)
async def drafts(request: Request):
    return templates.TemplateResponse("drafts.html", {
        "request": request,
        "year": CFP_DATA["year"],
        "title": CFP_DATA["title"],
        "drafts": DRAFTS
    })


@app.post("/drafts/{draft_id}/approve")
async def approve_draft(draft_id: str):
    for index, draft in enumerate(DRAFTS):
        if draft["id"] == draft_id:
            event = {
                "name": draft["name"],
                "link": draft["link"],
                "deadline": draft.get("deadline"),
                "event_date": draft.get("event_date")
            }
            EVENTS.append(event)
            CFP_DATA["events"] = EVENTS
            save_events()
            DRAFTS.pop(index)
            save_drafts(DRAFTS)
            return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)
    raise HTTPException(status_code=404, detail="Draft not found")
