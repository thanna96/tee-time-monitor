"""Utility helpers for tee time monitoring."""

from datetime import date, timedelta
from typing import Iterator


def date_range(start: date, days: int) -> Iterator[date]:
    """Generate a range of dates starting from ``start`` for ``days`` days."""
    for i in range(days):
        yield start + timedelta(days=i)