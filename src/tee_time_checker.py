"""Logic to query the tee time API and extract available times."""
from datetime import date
from typing import List

import requests

import config


def get_available_tee_times(day: date) -> List[str]:
    """Return a list of available tee time strings for the given date."""
    url = config.FOREUP_API_BASE.format(location_id=config.LOCATION_ID)
    params = {"date": day.isoformat()}
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    times = []
    for slot in data.get("tee_times", []):
        if slot.get("available"):
            times.append(slot.get("time"))
    return times