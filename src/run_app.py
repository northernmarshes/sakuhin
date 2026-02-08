import os
import threading
import time
import webbrowser
from django.core.management import execute_from_command_line


def run():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    execute_from_command_line(["manage.py", "runsever", "127.0.0.1:8000"])


if __name__ == "__main__":
    t = threading.Thread(target=run, deamon=True)
    t.start()
    time.sleep(2)
    webbrowser.open("http://127.0.0.1:8000")
    t.join()
