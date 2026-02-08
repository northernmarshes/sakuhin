import webview
import threading
import time
import sys
import os
from pathlib import Path
import shutil

BASE_DIR = Path(__file__).resolve().parent
SRC_DIR = BASE_DIR / "src"

if getattr(sys, "frozen", False):
    BASE_DIR = Path(sys._MEIPASS)

    if sys.platform == "win32":
        DATA_DIR = Path(os.getenv("APPDATA")) / "Archive"
    elif sys.platform == "darwin":
        DATA_DIR = Path.home() / "Library" / "Application Support" / "Archive"
    else:
        DATA_DIR = Path.home() / ".archive"

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    db_source = BASE_DIR / "src" / "db.sqlite3"
    db_dest = DATA_DIR / "db.sqlite3"
    if not db_dest.exists() and db_source.exists():
        shutil.copy2(db_source, db_dest)

    MEDIA_DIR = DATA_DIR / "media"
    MEDIA_DIR.mkdir(exist_ok=True)

else:
    BASE_DIR = Path(__file__).resolve().parent
    DATA_DIR = BASE_DIR / "src"
    MEDIA_DIR = DATA_DIR / "media"

SRC_DIR = BASE_DIR / "src"
sys.path.insert(0, str(SRC_DIR))


def run_django_server():
    os.chdir(SRC_DIR)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    os.environ["ARCHIVE_MEDIA_ROOT"] = str(MEDIA_DIR)

    try:
        from django.core.management import execute_from_command_line

        execute_from_command_line(["manage.py", "migrate", "--noinput"])

        execute_from_command_line(
            [
                "manage.py",
                "runserver",
                "--noreload",
                "--insecure",
                "127.0.0.1:8000",
            ]
        )
    except Exception as e:
        print(f"Error: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)


def main():
    django_thread = threading.Thread(target=run_django_server, daemon=True)
    django_thread.start()
    time.sleep(4)
    window = webview.create_window(
        title="Archive",
        url="http://127.0.0.1:8000",
        width=1400,
        height=900,
        resizable=True,
        fullscreen=False,
        min_size=(1000, 700),
        background_color="#FFFFFF",
    )
    webview.start(debug=False)


if __name__ == "__main__":
    main()
