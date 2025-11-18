

from typing import Union
from fastapi import FastAPI

app = FastAPI()

SPEAKER_APPLICATIONS = {
    "year": 2026,
    "title": "Speaker Applications",
    "events": [
        {
            "name": "PyCon Philippines",
            "link": "https://x.com/pyconph/status/1973342138042818835?s=46"
        },
        {
            "name": "PyCon Philippines (LinkedIn Post)",
            "link": "https://www.linkedin.com/posts/thokomiya_october2025-activity-7379415290230607873-pV9z"
        },
        {
            "name": "WeAreDevelopers World Congress 2026 Europe",
            "link": "https://sessionize.com/wearedevelopers-world-congress-2026-europe"
        },
        {
            "name": "WeAreDevelopers World Congress 2026 US",
            "link": "https://sessionize.com/wearedevelopers-world-congress-2026-us"
        },
        {
            "name": "PyCascades",
            "link": "https://www.pycascades.com/news/cfp-review/"
        },
        {
            "name": "PyCon DE",
            "link": "https://2026.pycon.de"
        },
        {
            "name": "Function Conference",
            "link": "https://fnctn1.com/"
        },
        {
            "name": "PG Data 2026",
            "link": "https://sessionize.com/pg-data-2026"
        },
        {
            "name": "PyCascades 2026 (Pretalx)",
            "link": "https://pretalx.com/pycascades-2026/cfp"
        },
        {
            "name": "FOSDEM 2026 Devrooms",
            "link": "https://fosdem.org/2026/news/2025-10-31-devrooms-announced/"
        }
    ]
}


@app.get("/")
def read_root():
    return SPEAKER_APPLICATIONS


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
