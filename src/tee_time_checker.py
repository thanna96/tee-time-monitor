"""Logic to query the tee time API and extract available times."""
from datetime import date
from typing import List, Optional

import requests

import config


def get_available_tee_times(
    day: date,
    *,
    course: Optional[str] = None,
    start_hour: Optional[int] = None,
    end_hour: Optional[int] = None,
) -> List[str]:
    """Return a list of available tee time strings for the given date.

    The optional ``course`` argument will filter the results to a specific
    course name if provided. ``start_hour`` and ``end_hour`` can be used to
    restrict the results to times within the given hour range.
    """

    url = config.FOREUP_API_BASE.format(location_id=config.LOCATION_ID)
    params = {"date": day.isoformat()}
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    times: List[str] = []
    for slot in data.get("tee_times", []):
        if not slot.get("available"):
            continue

        slot_time = slot.get("time")
        slot_course = slot.get("course")

        if course and course != slot_course:
            continue

        if slot_time and (start_hour is not None or end_hour is not None):
            try:
                hour = int(str(slot_time).split(":", 1)[0])
            except (ValueError, AttributeError):
                hour = None
            if hour is not None:
                if start_hour is not None and hour < start_hour:
                    continue
                if end_hour is not None and hour > end_hour:
                    continue

        if slot_time:
            times.append(slot_time)

    return times