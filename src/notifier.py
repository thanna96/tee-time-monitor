"""Email notification helpers."""
from email.mime.text import MIMEText
import os
import smtplib

import config


def has_subscribers() -> bool:
    """Return ``True`` if at least one email is stored."""
    if not os.path.exists(config.EMAIL_LIST_FILE):
        return False
    with open(config.EMAIL_LIST_FILE) as fh:
        for line in fh:
            if line.strip():
                return True
    return False


def _default_recipients() -> list[str]:
    emails: list[str] = []
    if os.path.exists(config.EMAIL_LIST_FILE):
        with open(config.EMAIL_LIST_FILE) as fh:
            for line in fh:
                line = line.strip()
                if line:
                    emails.append(line)
    if not emails:
        emails.append(config.EMAIL_TO)
    return emails


def send_email(subject: str, body: str, recipient=None) -> None:
    """Send an email with the given ``subject`` and ``body``."""
    if recipient is None:
        recipients = _default_recipients()
    elif isinstance(recipient, str):
        recipients = [recipient]
    else:
        recipients = list(recipient)

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = config.EMAIL_FROM
    msg["To"] = ", ".join(recipients)

    with smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT) as server:
        server.starttls()
        server.login(config.EMAIL_FROM, config.EMAIL_PASS)
        server.sendmail(config.EMAIL_FROM, recipients, msg.as_string())