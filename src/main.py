"""Entry point for monitoring tee times over a date range."""
from datetime import date

import config
from notifier import send_email
from tee_time_checker import get_available_tee_times
from utils import date_range


def monitor() -> None:
    """Check tee times for the configured date range and notify if available."""
    today = date.today()
    for day in date_range(today, config.CHECK_DAYS):
        times = get_available_tee_times(day)
        if times:
            body = "Available tee times:\n" + "\n".join(times)
            send_email(
                subject=f"Tee times for {day.isoformat()}",
                body=body,
            )


if __name__ == "__main__":
    monitor()