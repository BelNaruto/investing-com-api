"""Print this week's high-impact economic events (Investing.com economic calendar).

Get your key: https://rapidapi.com/belchiorarkad-FqvHs2EDOtP/api/investing-com-ultimate-api
Usage:  RAPIDAPI_KEY=xxx python economic_calendar.py US,EU
"""
import json
import os
import sys
from datetime import date, timedelta

import requests

HOST = "investing-com-ultimate-api.p.rapidapi.com"
HEADERS = {"X-RapidAPI-Key": os.environ["RAPIDAPI_KEY"], "X-RapidAPI-Host": HOST}

countries = sys.argv[1] if len(sys.argv) > 1 else "US"
today = date.today()

resp = requests.get(
    f"https://{HOST}/v2/calendars/economic",
    headers=HEADERS,
    params={
        "from": today.isoformat(),
        "to": (today + timedelta(days=7)).isoformat(),
        "countries": countries,
        "importance": "high",
    },
    timeout=30,
)
resp.raise_for_status()
print(json.dumps(resp.json(), indent=2, ensure_ascii=False))
