"""Simple web frontend for collecting subscriber emails."""
import os
from flask import Flask, request, send_from_directory, jsonify

from course_fetcher import fetch_courses

EMAIL_LIST_FILE = os.getenv("EMAIL_LIST_FILE", "emails.txt")

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
    line = f"{email},{course},{start_hour},{end_hour}\n"
    with open(EMAIL_LIST_FILE, "a") as fh:
        fh.write(line)
    return jsonify({"message": "Subscription saved!"})


@app.route("/courses")
def courses():
    """Return a list of course names scraped from the booking page."""
    return jsonify(fetch_courses())

if __name__ == "__main__":
    app.run(debug=True)