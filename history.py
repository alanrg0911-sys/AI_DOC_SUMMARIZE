from datetime import datetime
import json
from pathlib import Path

HISTORY_FILE = Path("/home/alan-rodriguez/Desktop/AI_DOC_SUMMARIZE/log/history.json")

def save_history(filename):

    try:
        with open (HISTORY_FILE, "r") as file:
            history = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        history = []

    for entry in history:
        if entry["filename"] == filename:
            entry["last_summarized"] == datetime.now().strftime("%Y-%M-%D-%H-%M")

            with open(HISTORY_FILE, "w") as file:
                json.dump(history, file, indent=4)

            return

    history.append({
            "id":len(history)+1,
            "filename":filename,
            "last_summarized":datetime.now().strftime("%Y-%M-%D")
                })

    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)

def view_history(HISTORY_FILE):

    try:
        with open (HISTORY_FILE, "r") as file:
            HISTORY_FILE.json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print(HISTORY_FILE)
            