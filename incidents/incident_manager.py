import json
from datetime import datetime
from pathlib import Path

LOG_FILE = Path("logs/incidents.json")


def log_incident(result):

    incident = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "container": result["container"],
        "action": result["action"],
        "status": "Success" if result["success"] else "Failed",
        "message": result["message"]
    }

    try:
        with open(LOG_FILE, "r") as file:
            incidents = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        incidents = []

    incidents.append(incident)

    with open(LOG_FILE, "w") as file:
        json.dump(incidents, file, indent=4)

    return incident


def get_incidents():

    try:
        with open(LOG_FILE, "r") as file:
            incidents = json.load(file)

            return incidents[::-1]

    except (FileNotFoundError, json.JSONDecodeError):

        return []