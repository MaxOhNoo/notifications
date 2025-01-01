from flask import Flask, jsonify, redirect, render_template, request, url_for
from plyer import notification

app = Flask(__name__)


@app.route("/toast", methods=["GET", "POST"])
def make_toast():
    if request.method == "GET":
        return redirect(url_for("index"))
    data = request.form
    title, message = data["title"], data["message"]
    message = data["message"]
    if title == "":
        title = "Missing title"
    if message == "":
        message = "Missing message"
    notify(message, title)
    success = True
    return jsonify({"success": success, "title": title, "message": message})


def notify(message, title):
    notification.notify(
        title=title,
        message=message,
        timeout=100,
    )


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
