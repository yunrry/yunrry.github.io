import os
import yaml

BASE_DIR = "assets/contents"
OUTPUT_FILE = "_data/contents.yml"

def load_existing_data():
    """기존 YAML 파일 로드"""
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or []
    return []

def get_category_from_path(path):
    """경로에서 category 추출 (contents 다음의 첫 번째 디렉토리)"""
    parts = path.replace("\\", "/").split("/")
    try:
        idx = parts.index("contents")
        return parts[idx + 1]
    except (ValueError, IndexError):
        return "uncategorized"

def get_category2_from_path(path):
    """경로에서 category2 추출 (contents 다음의 두 번째 디렉토리 또는 파일명)"""
    parts = path.replace("\\", "/").split("/")
    try:
        idx = parts.index("contents")
        # contents 다음에 두 번째 요소가 있으면 그것을, 없으면 파일명(확장자 제외)을 반환
        if len(parts) > idx + 2:
            return parts[idx + 2]
        else:
            # 파일명에서 확장자 제거
            filename = parts[-1]
            return os.path.splitext(filename)[0]
    except (ValueError, IndexError):
        return "uncategorized"

def update_categories():
    """contents.yml의 모든 항목에 대해 category와 category2 업데이트"""
    # 기존 데이터 로드
    contents = load_existing_data()
    
    if not contents:
        print("⚠️  contents.yml 파일이 없거나 비어있습니다.")
        return
    
    updated_count = 0
    
    # 각 항목의 category와 category2 업데이트
    for item in contents:
        file_path = item.get("path", "")
        
        # 파일이 실제로 존재하는지 확인
        if not os.path.exists(file_path):
            print(f"⚠️  파일이 존재하지 않습니다: {file_path}")
            continue
        
        # 경로에서 category와 category2 재계산
        new_category = get_category_from_path(file_path)
        new_category2 = get_category2_from_path(file_path)
        
        # 변경사항이 있는지 확인
        old_category = item.get("category", "")
        old_category2 = item.get("category2", "")
        
        if old_category != new_category or old_category2 != new_category2:
            item["category"] = new_category
            item["category2"] = new_category2
            updated_count += 1
            print(f"✅ 업데이트: {file_path}")
            print(f"   category: {old_category} -> {new_category}")
            print(f"   category2: {old_category2} -> {new_category2}")
    
    # 업데이트된 내용을 파일에 저장
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        yaml.dump(contents, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    
    print(f"\n✅ {OUTPUT_FILE} 업데이트 완료")
    print(f"   총 {len(contents)}개 항목 중 {updated_count}개 항목의 category/category2 업데이트됨")

if __name__ == "__main__":
    update_categories()