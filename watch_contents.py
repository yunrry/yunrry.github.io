import time
import subprocess
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

WATCH_DIR = "assets/contents"
GENERATE_SCRIPT = "generate_contents_yaml.py"
JEKYLL_PID_FILE = ".jekyll_pid"

def restart_jekyll():
    """Jekyll 서버 재시작"""
    # Jekyll 프로세스 종료
    if os.path.exists(JEKYLL_PID_FILE):
        with open(JEKYLL_PID_FILE, 'r') as f:
            pid = f.read().strip()
        if pid:
            try:
                os.kill(int(pid), 15)  # SIGTERM
                time.sleep(1)
                os.kill(int(pid), 9)   # SIGKILL
            except (ProcessLookupError, ValueError):
                pass
    
    # 잔여 프로세스 정리
    subprocess.run(["pkill", "-f", "jekyll serve"], check=False)
    time.sleep(1)
    
    # 재시작
    process = subprocess.Popen(
        ["bundle", "exec", "jekyll", "serve", "--livereload"],
        stdout=open("/tmp/jekyll.log", "a"),
        stderr=subprocess.STDOUT
    )
    with open(JEKYLL_PID_FILE, 'w') as f:
        f.write(str(process.pid))
    print("♻️  Jekyll 서버 재시작 완료\n")

class ChangeHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.src_path.endswith(".md") and event.event_type in ['modified', 'created', 'deleted']:
            print(f"🔄 변경 감지: {event.src_path}")
            subprocess.run(["python3", GENERATE_SCRIPT])
            restart_jekyll()

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