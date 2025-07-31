# Tee Time Watcher

A simple utility to monitor golf tee time availability and send email updates.

## Requirements

- Python 3.11+
- `pip`

## Setup

1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Create a `.env` file with your credentials:

```
EMAIL_FROM=example@gmail.com
EMAIL_PASS=secret
EMAIL_TO=notify@example.com  # fallback
LOCATION_ID=12345
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
FOREUP_API_BASE=https://foreup.example.com/api/location/{location_id}/times
CHECK_DAYS=7
EMAIL_LIST_FILE=emails.txt
```

3. (Optional) start the web front end to collect subscriber emails:

```bash
python -m src.web
```

Visit `http://localhost:5000` and submit an email address to store it in `EMAIL_LIST_FILE`.

4. Run the monitor locally:

```bash
python -m src.main
```

## Deployment

Wrappers for AWS Lambda and Google Cloud Functions are included in `deploy/`.

### AWS Lambda

1. Zip the project files and install dependencies into the archive.
2. Create a Lambda function with the Python runtime (3.11) and upload the zip.
3. Set environment variables as shown in the `.env` file.
4. Use `deploy/aws_lambda/handler.lambda_handler` as the function handler.

### Google Cloud Functions

1. Deploy a new function using Python 3.11.
2. Use `deploy/gcp_function/main.py` with entry point `main`.
3. Configure the same environment variables.

Both platforms require outbound internet access so the function can reach the ForeUP API and your SMTP server.

## API Keys and Configuration

- **ForeUP API**: Set `LOCATION_ID` to your course identifier and `FOREUP_API_BASE` to the base endpoint. If an API key is required, include it in this URL.
- **Email account**: `EMAIL_FROM` and `EMAIL_PASS` should correspond to an SMTP account capable of sending mail. Adjust `SMTP_SERVER` and `SMTP_PORT` as needed.

Subscribed addresses are stored in `EMAIL_LIST_FILE`. If this file is empty the `EMAIL_TO` address will be used as a fallback.