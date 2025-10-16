import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

WATCH_DIR = "assets/contents"
GENERATE_SCRIPT = "generate_contents_yaml.py"

class ChangeHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.src_path.endswith(".md"):
            print(f"🔄 변경 감지: {event.src_path}")
            subprocess.run(["python3", GENERATE_SCRIPT])

if __name__ == "__main__":
    observer = Observer()
    handler = ChangeHandler()
    observer.schedule(handler, WATCH_DIR, recursive=True)
    observer.start()
    print(f"👀 {WATCH_DIR} 변경 감시 중... (Ctrl+C로 중단)")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
