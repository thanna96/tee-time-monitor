"""AWS Lambda entry point."""
from src.main import monitor


def lambda_handler(event, context):
    monitor()
    return {"status": "ok"}