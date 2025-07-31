"""Configuration for tee time monitoring."""
import os

LOCATION_ID = os.getenv("LOCATION_ID", "12345")
EMAIL_FROM = os.getenv("EMAIL_FROM", "your_email@example.com")
EMAIL_TO = os.getenv("EMAIL_TO", "notify@example.com")
EMAIL_PASS = os.getenv("EMAIL_PASS", "password")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))

CHECK_DAYS = int(os.getenv("CHECK_DAYS", "7"))
FOREUP_API_BASE = os.getenv(
    "FOREUP_API_BASE",
    "https://foreup.example.com/api/location/{location_id}/times"
)

EMAIL_LIST_FILE = os.getenv("EMAIL_LIST_FILE", "emails.txt")
