#!/bin/bash
# ======================================
# Jekyll + Markdown Watch + Auto Restart
# ======================================

set -e

WATCH_DIR="assets/contents"
PYTHON_SCRIPT="watch_contents.py"
VENV_DIR="venv"
JEKYLL_PID_FILE=".jekyll_pid"

# ... existing code for Python/Ruby check and venv setup ...

# Jekyll 프로세스 종료 함수
stop_jekyll() {
  if [ -f "$JEKYLL_PID_FILE" ]; then
    local pid=$(cat "$JEKYLL_PID_FILE" 2>/dev/null)
    if [ -n "$pid" ] && kill -0 "$pid" 2>/dev/null; then
      echo "🛑 Jekyll 프로세스 종료 중 (PID: $pid)..."
      kill "$pid" 2>/dev/null || true
      sleep 1
      kill -9 "$pid" 2>/dev/null || true
    fi
    rm -f "$JEKYLL_PID_FILE"
  fi
  pkill -f "jekyll serve" 2>/dev/null || true
}

# Jekyll 서버 실행 함수
run_jekyll() {
  stop_jekyll
  echo "🔧 Jekyll 서버 실행 중..."
  bundle exec jekyll serve --livereload > /tmp/jekyll.log 2>&1 &
  local jekyll_pid=$!
  echo $jekyll_pid > "$JEKYLL_PID_FILE"
  echo "✅ Jekyll 서버 시작됨 (PID: $jekyll_pid)"
  sleep 2
}

# 프로세스 종료 시 정리
cleanup() {
  echo "🛑 종료 중..."
  stop_jekyll
  pkill -f "watch_contents.py" 2>/dev/null || true
  deactivate 2>/dev/null || true
  exit 0
}
trap cleanup INT TERM

# 재시작 함수 (외부에서 호출 가능하도록)
export -f stop_jekyll run_jekyll
export JEKYLL_PID_FILE

# 초기 실행
run_jekyll

# watch_contents.py 수정하여 재시작 로직 추가
python3 "$PYTHON_SCRIPT" &
WATCHER_PID=$!

# 메인 프로세스 대기
wait