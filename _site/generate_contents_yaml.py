import os
import yaml
from datetime import datetime

# 대상 디렉토리와 출력 파일 경로
BASE_DIR = "assets/contents"
OUTPUT_FILE = "_data/contents.yml"

def get_file_dates(path):
    """파일의 생성일(created)과 수정일(updated) 가져오기"""
    stat = os.stat(path)
    created = datetime.fromtimestamp(stat.st_ctime).strftime("%Y-%m-%d")
    updated = datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d")
    return created, updated

def get_title_from_md(path):
    """Markdown 파일에서 첫 번째 헤더(# )를 title로 추출"""
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip().startswith("# "):
                return line.strip().lstrip("# ").strip()
    return os.path.basename(path)  # 헤더 없을 경우 파일명 반환

def get_category_from_path(path):
    """path에서 contents/ 다음 하위 폴더 이름 추출"""
    parts = path.replace("\\", "/").split("/")
    try:
        idx = parts.index("contents")
        return parts[idx + 1]  # contents 바로 다음 폴더 이름
    except (ValueError, IndexError):
        return "uncategorized"

def main():
    contents = []
    for root, _, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, ".").replace("\\", "/")
                title = get_title_from_md(full_path)
                created, updated = get_file_dates(full_path)
                category = get_category_from_path(rel_path)

                contents.append({
                    "path": rel_path,
                    "title": title,
                    "category": category,
                    "created": created,
                    "updated": updated,
                })

    # 날짜순 정렬 (최신순)
    contents.sort(key=lambda x: x["created"], reverse=True)

    # YAML 파일로 저장
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        yaml.dump(contents, f, allow_unicode=True, sort_keys=False)

    print(f"✅ {OUTPUT_FILE} 생성 완료 ({len(contents)}개 항목)")

if __name__ == "__main__":
    main()
