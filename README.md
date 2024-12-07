# 📚 Book-Hunting-Librarian

![image](https://github.com/user-attachments/assets/ff594222-892a-4b3d-b51f-86d878f8cec3)

`책찾사`는 `책을 찾아주는 사서`의 줄임말로 Discord를 통해 책을 검색하고, 북마크를 관리할 수 있는 강력한 도서 검색 봇입니다. 네이버 책 검색 API를 활용하여 원하는 도서를 손쉽게 찾고 관리할 수 있습니다. 테스트를 위해 env파일도 같이 배포합니다.

---

## 📜 목차

1. [🛠️ 프로젝트 프로그램 설치방법](🛠️-프로젝트-프로그램-설치방법)
2. [📂 프로젝트 구성](#📂-프로젝트-구성)
3. [🎮 프로젝트 프로그램 사용법](#🎮-프로젝트-프로그램-사용법)
   - [명령어 목록](#명령어-목록)
4. [🛡️ 저작권 및 사용권 정보](#️🛡️-저작권-및-사용권-정보)

---

## 🛠️ 프로젝트 프로그램 설치방법

1. **레포지토리 클론**

   ```bash
   git clone https://github.com/your-repository/book-hunting-librarian.git
   cd book-hunting-librarian
   ```

2. **필수 패키지 설치**

   ```bash
   pip install -r requirements.txt
   ```

3. **python 실행**
   ```bash
   python bot.py
   ```
4. **discord bot 초대**

   [책찾사 초대하기](https://discord.com/oauth2/authorize?client_id=1303917514413310043&permissions=0&integration_type=0&scope=bot)
   링크 클릭 후 서버 선택해서 초대하기

## 📂 프로젝트 구성

```plaintext
📂BOOK-HUNTING-LIBRARIAN
├── book_search.py          # 네이버 API와 연동하여 책을 검색하는 함수
├── bookmark_manager.py     # 북마크 데이터를 관리하는 함수
├── bookmark_view.py        # 북마크 삭제 버튼 구현
├── category_view.py        # 카테고리 선택 View 구현
├── bot.py                  # Discord 봇 메인 코드
├── bookmarks.json          # 사용자별 북마크 데이터를 저장하는 JSON 파일
├── requirements.txt        # 필요한 Python 패키지 목록
├── .env                    # 환경 변수 파일 (토큰 및 API 키 저장)
├── LICENSE                 # 프로젝트 라이선스
└── README.md               # 프로젝트 설명 파일
```

## 🎮 프로젝트 프로그램 사용법

### 명령어 목록

`!도서제목 [제목]`: 입력한 제목으로 책을 검색합니다.

```bash
!도서제목 린치핀
```

<img width="366" alt="image" src="https://github.com/user-attachments/assets/fc0cd9ac-cd77-413b-b7e2-be17434d05d7">

`!도서작가 [작가명]`: 입력한 작가명으로 책을 검색합니다.

```bash
!도서작가 그레고리 머과이어
```

<img width="412" alt="image" src="https://github.com/user-attachments/assets/59bc1396-e520-4937-b1f4-02609dbc6848">

`!도서카테고리`: 카테고리 선택 버튼을 통해 책을 검색합니다.

```
!도서카테고리
```

<img width="493" alt="image" src="https://github.com/user-attachments/assets/c533185b-b922-4011-abea-0e971dc7b209">

`!북마크추가 [제목]`: 입력한 제목으로 검색한 첫 번째 결과를 북마크에 추가합니다.

```bash
!북마크추가 린치핀
```

<img width="432" alt="image" src="https://github.com/user-attachments/assets/5e39da3f-4038-4ae2-a5e5-b7cb7e40227b">

`!북마크목록`: 북마크에 저장된 책 목록을 확인합니다. 각 북마크에는 삭제 버튼이 포함됩니다.

```
!북마크목록
```

<img width="381" alt="image" src="https://github.com/user-attachments/assets/8ed27ece-968d-4846-8224-e853696cd276">

`!도움말`: 사용 가능한 모든 명령어와 설명을 표시합니다.

```
!도움말
```

<img width="391" alt="image" src="https://github.com/user-attachments/assets/330fee5e-3223-403c-8a2d-925ec63ea88f">

## 🛡️ 저작권 및 사용권 정보

이 프로젝트는 `MIT License`를 따릅니다. 자유롭게 사용하고 수정할 수 있으나, 반드시 원작자의 저작권 표시를 유지해야 합니다.
