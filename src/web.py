"""Simple web frontend for collecting subscriber emails."""
import os
from datetime import date
from threading import Thread
from flask import Flask, request, send_from_directory, jsonify

import config
from course_fetcher import fetch_courses
from tee_time_checker import get_available_tee_times
from main import monitor
from notifier import has_subscribers

EMAIL_LIST_FILE = config.EMAIL_LIST_FILE

app = Flask(__name__, static_folder="../frontend/dist", static_url_path="")

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/subscribe", methods=["POST"])
def subscribe():
    data = request.get_json(force=True)
    email = (data.get("email") or "").strip()
    course = data.get("course", "").strip()
    start_hour = data.get("startHour", "")
    end_hour = data.get("endHour", "")
    if not email:
        return jsonify({"message": "No email provided."}), 400
    is_first = not has_subscribers()
    line = f"{email},{course},{start_hour},{end_hour}\n"
    with open(EMAIL_LIST_FILE, "a") as fh:
        fh.write(line)
    if is_first:
        Thread(target=monitor, daemon=True).start()
    return jsonify({"message": "Subscription saved!"})


@app.route("/courses")
def courses():
    """Return a list of course names scraped from the booking page."""
    return jsonify(fetch_courses())


@app.route("/times")
def times():
    """Return available tee times for a given date and optional filters."""
    day_str = request.args.get("date", "")
    if not day_str:
        return jsonify({"error": "Missing date"}), 400
    try:
        day = date.fromisoformat(day_str)
    except ValueError:
        return jsonify({"error": "Invalid date"}), 400

    course = request.args.get("course") or None
    try:
        start_hour = int(request.args.get("startHour"))
    except (TypeError, ValueError):
        start_hour = None
    try:
        end_hour = int(request.args.get("endHour"))
    except (TypeError, ValueError):
        end_hour = None

    times = get_available_tee_times(
        day,
        course=course,
        start_hour=start_hour,
        end_hour=end_hour,
    )
    return jsonify(times)

if __name__ == "__main__":
    app.run(debug=True)