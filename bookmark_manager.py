import json

# 북마크 파일 경로
BOOKMARK_FILE = "bookmarks.json"

# 북마크 데이터를 로드하는 함수
def load_bookmarks():
    try:
        with open(BOOKMARK_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}  # 파일이 없으면 빈 딕셔너리 반환
    except json.JSONDecodeError:
        return {}  # 파일 내용이 손상된 경우 빈 딕셔너리 반환

# 북마크 데이터를 저장하는 함수
def save_bookmarks(bookmarks):
    with open(BOOKMARK_FILE, "w", encoding="utf-8") as f:
        json.dump(bookmarks, f, indent=4, ensure_ascii=False)
