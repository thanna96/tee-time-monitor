"""Utility to retrieve course names using the ForeUP API."""
from __future__ import annotations

from typing import List
from datetime import date

import requests

import config


def fetch_courses() -> List[str]:
    """Fetch available course names from the ForeUP API.

    The previous implementation scraped the booking page which is brittle and
    often blocked by ForeUP. This version queries the tee time API for today's
    date and extracts the unique course names from the response.
    """

    url = config.FOREUP_API_BASE.format(location_id=config.LOCATION_ID)
    params = {"date": date.today().isoformat()}
    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
    except Exception:
        return []

    data = resp.json()
    courses = {
        slot.get("course")
        for slot in data.get("tee_times", [])
        if slot.get("course")
    }
    return sorted(courses)