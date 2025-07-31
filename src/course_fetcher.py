"""Utility to scrape course names from the ForeUP booking page."""
from __future__ import annotations

from typing import List

import requests
from bs4 import BeautifulSoup

import config


def fetch_courses() -> List[str]:
    """Fetch and parse course names from the configured booking page."""
    url = config.FOREUP_BOOKING_URL
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
    except Exception:
        return []

    soup = BeautifulSoup(resp.text, "html.parser")
    courses: List[str] = []
    for select in soup.find_all("select"):
        attr = (select.get("id", "") + select.get("name", "")).lower()
        if "course" in attr or "park" in attr:
            for option in select.find_all("option"):
                val = option.get("value", "").strip()
                text = option.text.strip()
                if val and text:
                    courses.append(text)
    return courses