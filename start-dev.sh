#!/bin/bash
# ======================================
# Jekyll + Markdown Watch + Auto Restart
# ======================================

set -e

WATCH_DIR="assets/contents"
PYTHON_SCRIPT="watch_contents.py"
VENV_DIR="venv"

# Python 및 Ruby 환경 확인
if ! command -v python3 &> /dev/null; then
  echo "❌ Python3 not found. 설치 후 다시 시도하세요."
  exit 1
fi

if ! command -v bundle &> /dev/null; then
  echo "❌ Bundler not found. Ruby 환경을 먼저 설정하세요."
  exit 1
fi

# venv 확인 및 활성화
if [ ! -d "$VENV_DIR" ]; then
  echo "📦 venv가 없습니다. 생성 중..."
  python3 -m venv "$VENV_DIR"
  echo "✅ venv 생성 완료"
fi

echo "🐍 venv 활성화 중..."
source "$VENV_DIR/bin/activate"

# watchdog 설치 확인
if ! python3 -c "import watchdog" 2>/dev/null; then
  echo "📥 watchdog 설치 중..."
  pip install watchdog
fi

echo "🚀 개발 서버 시작 중..."
echo "   - Markdown 감시 (${WATCH_DIR})"
echo "   - Jekyll 서버 (자동 재시작 지원)"

# 프로세스 종료 시 둘 다 정리
cleanup() {
  echo "🛑 종료 중..."
  pkill -f "jekyll" || true
  pkill -f "${PYTHON_SCRIPT}" || true
  deactivate 2>/dev/null || true
  exit 0
}
trap cleanup INT TERM

# Jekyll 서버 실행 함수
run_jekyll() {
  echo "🔧 Jekyll 서버 실행 중..."
  bundle exec jekyll serve --livereload &
  echo $! > .jekyll_pid
}

# Markdown 감시 함수 (파일 변경 시 Jekyll 재시작)
run_watcher() {
  python3 - <<'EOF'
import subprocess, time, os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

WATCH_DIR = "assets/contents"
GENERATE_SCRIPT = "generate_contents_yaml.py"

class Handler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.src_path.endswith(".md"):
            print(f"🔄 변경 감지: {event.src_path}")
            subprocess.run(["python3", GENERATE_SCRIPT])
            # Jekyll PID 읽어서 재시작
            if os.path.exists(".jekyll_pid"):
                with open(".jekyll_pid") as f:
                    pid = f.read().strip()
                try:
                    subprocess.run(["kill", "-HUP", pid])
                    print("♻️  Jekyll 서버 재시작 완료\n")
                except Exception as e:
                    print("⚠️  Jekyll 재시작 실패:", e)

observer = Observer()
observer.schedule(Handler(), WATCH_DIR, recursive=True)
observer.start()
print(f"👀 {WATCH_DIR} 감시 중... (Ctrl+C로 중단)")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
EOF
}

# 초기 실행
run_jekyll
run_watcher