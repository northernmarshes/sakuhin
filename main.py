import subprocess
import webview
import sys
import os
import threading
import time

# Catalogue path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, "src")

# Making sure database exists
DB_DIR = os.path.join(BASE_DIR, "db")
os.makedirs(DB_DIR, exist_ok=True)


def run_django():
    os.chdir(SRC_DIR)
    subprocess.run([sys.executable, "manage.py", "runserver", "127.0.0.1:8000"])


# Starting django in a separete thread
thread = threading.Thread(target=run_django, daemon=True)
thread.start()

# Waiting
time.sleep(2)

# Opening GUI in PyView
webview.create_window("Sakuhin", "http://127.0.0.1:8000")
webview.start()
