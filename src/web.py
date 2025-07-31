"""Simple web frontend for collecting subscriber emails."""
import os
from flask import Flask, request, render_template_string

EMAIL_LIST_FILE = os.getenv("EMAIL_LIST_FILE", "emails.txt")

app = Flask(__name__)

INDEX_TEMPLATE = """
<!doctype html>
<title>Subscribe for Tee Time Alerts</title>
<h1>Subscribe for Tee Time Alerts</h1>
<form method="post" action="/subscribe">
  <input type="email" name="email" placeholder="Enter your email" required />
  <button type="submit">Subscribe</button>
</form>
{% if message %}<p>{{ message }}</p>{% endif %}
"""


@app.route("/", methods=["GET"])
def index():
    return render_template_string(INDEX_TEMPLATE, message=None)


@app.route("/subscribe", methods=["POST"])
def subscribe():
    email = request.form.get("email")
    message = ""
    if email:
        with open(EMAIL_LIST_FILE, "a") as fh:
            fh.write(email.strip() + "\n")
        message = "Subscription saved!"
    else:
        message = "No email provided."
    return render_template_string(INDEX_TEMPLATE, message=message)


if __name__ == "__main__":
    app.run(debug=True)