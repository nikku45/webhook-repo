from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.json_util import dumps
from flask import render_template

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017")
db = client["github_events"]
collection = db["events"]

@app.route("/webhook", methods=["POST"])
def github_webhook():
    event_type = request.headers.get("X-GitHub-Event")
    payload = request.json

    clean_event = None

    # PUSH EVENT
    if event_type == "push":
        clean_event = {
            "author": payload.get("pusher", {}).get("name"),
            "action": "push",
            "from_branch": None,
            "to_branch": payload.get("ref", "").split("/")[-1],
            "timestamp": payload.get("head_commit", {}).get("timestamp")
        }

    # PULL REQUEST EVENT
    elif event_type == "pull_request":
        action = payload.get("action")

        # Only care when PR is opened
        if action == "opened":
            pr = payload.get("pull_request", {})
            clean_event = {
                "author": pr.get("user", {}).get("login"),
                "action": "pull_request",
                "from_branch": pr.get("head", {}).get("ref"),
                "to_branch": pr.get("base", {}).get("ref"),
                "timestamp": pr.get("created_at")
            }

    if clean_event:
        print("\nCLEAN EVENT DATA:",clean_event)
        eventId = collection.insert_one(clean_event).inserted_id
        print("Event saved with ID:", eventId)

    return jsonify({"status": "ok"}), 200

@app.route("/events", methods=["GET"])
def get_events():
    events = collection.find().sort("_id", -1).limit(10)
    return dumps(events), 200



@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=5000)
