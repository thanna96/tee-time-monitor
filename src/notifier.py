"""Email notification helpers."""
from email.mime.text import MIMEText
import smtplib

import config


def send_email(subject: str, body: str, recipient: str = None) -> None:
    """Send an email with the given ``subject`` and ``body``."""
    recipient = recipient or config.EMAIL_TO
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = config.EMAIL_FROM
    msg["To"] = recipient

    with smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT) as server:
        server.starttls()
        server.login(config.EMAIL_FROM, config.EMAIL_PASS)
        server.sendmail(config.EMAIL_FROM, [recipient], msg.as_string())
