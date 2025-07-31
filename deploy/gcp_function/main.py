+8
-0

"""Google Cloud Function entry point."""
from src.main import monitor


def main(request):
    monitor()
    return "ok"