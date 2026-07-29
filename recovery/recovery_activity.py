import json
from datetime import datetime
from pathlib import Path

LOG_FILE = Path("logs/recovery.json")


def log_recovery(result):

    recovery = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "container": result["container"],
        "action": result["action"],
        "status": "Success" if result["success"] else "Failed",
        "message": result["message"]
    }

    try:
        with open(LOG_FILE, "r") as file:
            recoveries = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        recoveries = []

    recoveries.append(recovery)

    with open(LOG_FILE, "w") as file:
        json.dump(recoveries, file, indent=4)

    return recovery


def get_recoveries():

    try:
        with open(LOG_FILE, "r") as file:
            recoveries = json.load(file)

        return recoveries[::-1]

    except (FileNotFoundError, json.JSONDecodeError):
        return []