import os
import threading
import time
import webbrowser
from django.core.management import execute_from_command_line
import subprocess

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

if not os.path.exists("db.sqlite3"):
    subprocess.run(["python", "manage.py", "migrate"])


def run():
    execute_from_command_line(["manage.py", "runserver", "127.0.0.1:8000"])


if __name__ == "__main__":
    t = threading.Thread(target=run, daemon=True)
    t.start()
    time.sleep(2)
    webbrowser.open("http://127.0.0.1:8000")
    t.join()
