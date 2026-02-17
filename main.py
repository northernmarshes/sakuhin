import subprocess
import webview
import sys
import os
import threading
import time
import requests

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, "src")
DB_DIR = os.path.join(BASE_DIR, "db")

# Making sure database exists
os.makedirs(DB_DIR, exist_ok=True)


def run_django():
    """Run Django server in the background."""
    os.chdir(SRC_DIR)
    subprocess.Popen([sys.executable, "manage.py", "runserver", "127.0.0.1:8000"])


# Start Django in a separate thread
thread = threading.Thread(target=run_django, daemon=True)
thread.start()

# Wait untill server is up
server_url = "http://127.0.0.1:8000"
while True:
    try:
        requests.get(server_url)
        break
    except requests.exceptions.ConnectionError:
        time.sleep(0.5)

# Open GUI in PyWebView
webview.create_window("Sakuhin", server_url)
webview.start()
