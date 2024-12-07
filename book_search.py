import os
import requests
from dotenv import load_dotenv

# .env 파일에서 환경 변수 불러오기
load_dotenv()
NAVER_CLIENT_ID = os.getenv("NAVER_CLIENT_ID")
NAVER_CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET")

def search_book_by_title(title):
    url = "https://openapi.naver.com/v1/search/book.json"
    headers = {
        "X-Naver-Client-Id": NAVER_CLIENT_ID,
        "X-Naver-Client-Secret": NAVER_CLIENT_SECRET
    }
    params = {"query": title}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        result = response.json()
        items = result.get("items")
        if items:
            # 필요한 정보만 추출하여 반환
            books = []
            for item in items:
                book = {
                    "title": item.get("title"),
                    "author": item.get("author"),
                    "image": item.get("image"),
                    "link": item.get("link")
                }
                books.append(book)
            return books
        else:
            return "No books found for the title."
    else:
        return f"Error: {response.status_code}"

# 작가 이름으로 도서 검색
def search_book_by_author(author):
    url = "https://openapi.naver.com/v1/search/book.json"
    headers = {
        "X-Naver-Client-Id": NAVER_CLIENT_ID,
        "X-Naver-Client-Secret": NAVER_CLIENT_SECRET
    }
    params = {"query": author}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        result = response.json()
        items = result.get("items")
        if items:
            books = []
            for item in items:
                book = {
                    "title": item.get("title"),
                    "author": item.get("author"),
                    "image": item.get("image"),
                    "link": item.get("link")
                }
                books.append(book)
            return books
        else:
            return "No books found for the author."
    else:
        return f"Error: {response.status_code}"
