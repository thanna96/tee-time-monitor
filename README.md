# Tee Time Watcher

A simple utility to monitor golf tee time availability. It queries a ForeUP-style API and sends an email when new tee times are found.

## Setup

1. Create a `.env` file with your credentials:

```
EMAIL_FROM=example@gmail.com
EMAIL_PASS=secret
EMAIL_TO=notify@example.com
LOCATION_ID=12345
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the monitor locally:

```bash
python -m src.main
```

## Deployment

The `deploy/` folder contains wrappers for AWS Lambda and Google Cloud Functions.
