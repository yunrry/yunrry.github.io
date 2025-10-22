import os
import yaml
from datetime import datetime

BASE_DIR = "assets/contents"
OUTPUT_FILE = "_data/contents.yml"

def load_existing_data():
    """기존 YAML 파일 로드"""
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
            return {item['path']: item for item in yaml.safe_load(f) or []}
    return {}

def get_file_dates(path):
    stat = os.stat(path)
    created = datetime.fromtimestamp(stat.st_ctime).strftime("%Y-%m-%d")
    updated = datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d")
    return created, updated

def get_title_from_md(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip().startswith("# "):
                return line.strip().lstrip("# ").strip()
    return os.path.basename(path)

def get_category_from_path(path):
    parts = path.replace("\\", "/").split("/")
    try:
        idx = parts.index("contents")
        return parts[idx + 1]
    except (ValueError, IndexError):
        return "uncategorized"

def main():
    existing = load_existing_data()
    current_files = set()
    
    for root, _, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, ".").replace("\\", "/")
                current_files.add(rel_path)
                
                # 기존 데이터가 있으면 유지, 없으면 새로 생성
                if rel_path not in existing:
                    title = get_title_from_md(full_path)
                    created, updated = get_file_dates(full_path)
                    category = get_category_from_path(rel_path)
                    
                    existing[rel_path] = {
                        "path": rel_path,
                        "title": title,
                        "category": category,
                        "created": created,
                        "updated": updated,
                    }
                else:
                    # 수정일만 업데이트
                    _, updated = get_file_dates(full_path)
                    existing[rel_path]["updated"] = updated
    
    # 삭제된 파일 제거
    existing = {k: v for k, v in existing.items() if k in current_files}
    
    # 리스트로 변환 후 날짜순 정렬
    contents = list(existing.values())
    contents.sort(key=lambda x: x["created"], reverse=True)
    
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        yaml.dump(contents, f, allow_unicode=True, sort_keys=False)
    
    print(f"✅ {OUTPUT_FILE} 생성 완료 ({len(contents)}개 항목)")

if __name__ == "__main__":
    main()