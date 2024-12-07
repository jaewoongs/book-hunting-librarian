import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from book_search import search_book_by_title, search_book_by_author
from bookmark_manager import load_bookmarks, save_bookmarks 
from bookmark_view import BookmarkDeletionView
from category_view import CategorySelectionView  # View 클래스 가져오기

# .env 파일에서 DISCORD_TOKEN 불러오기
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# 인텐트 설정 및 봇 초기화
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

# !도서제목 명령어 - 제목으로 도서 검색
@bot.command(name="도서제목")
async def book_title_search(ctx, *, title: str):
    books = search_book_by_title(title)
    
    if isinstance(books, str):  # 오류 메시지 처리
        await ctx.send(books)
    else:
        for book in books[:5]:  # 상위 5개 결과만 표시
            embed = discord.Embed(
                title=book["title"],
                url=book["link"],
                description=f"Author: {book['author']}",
                color=0x00c3ff
            )
            if book["image"]:
                embed.set_thumbnail(url=book["image"])
            await ctx.send(embed=embed)

# !도서작가 명령어 - 작가로 도서 검색
@bot.command(name="도서작가")
async def book_author_search(ctx, *, author: str):
    books = search_book_by_author(author)
    
    if isinstance(books, str):  # 오류 메시지 처리
        await ctx.send(books)
    else:
        for book in books[:5]:  # 상위 5개 결과만 표시
            embed = discord.Embed(
                title=book["title"],
                url=book["link"],
                description=f"Author: {book['author']}",
                color=0x00c3ff
            )
            if book["image"]:
                embed.set_thumbnail(url=book["image"])
            await ctx.send(embed=embed)


@bot.command(name="도서카테고리")
async def book_category_selection(ctx):
    # 제공할 카테고리 목록
    categories = ["소설", "시/에세이", "경제/경영", "자기계발", "인문", "역사", "사회/정치", "자연/과학", "예술/대중문화", "종교"]
    
    # 카테고리 선택 View 생성
    view = CategorySelectionView(ctx, categories)
    
    # 카테고리 선택 메시지와 함께 버튼 표시
    await ctx.send("검색할 카테고리를 선택해주세요:", view=view)

# !북마크추가 명령어 정의
@bot.command(name="북마크추가")
async def add_bookmark(ctx, *, book_title: str):
    # 네이버 API를 사용하여 책 검색
    books = search_book_by_title(book_title)

    if isinstance(books, str):  # 검색 결과가 문자열(오류 메시지)일 경우
        await ctx.send(books)
    else:
        if not books:
            await ctx.send(f"'{book_title}'에 대한 검색 결과가 없습니다.")
            return

        # 첫 번째 검색 결과 가져오기
        first_book = books[0]  # 첫 번째 책 정보
        user_id = str(ctx.author.id)  # 사용자 ID

        # 북마크 데이터 로드
        bookmarks = load_bookmarks()

        # 사용자 데이터 초기화
        if user_id not in bookmarks:
            bookmarks[user_id] = []

        # 첫 번째 검색 결과를 북마크에 추가
        if first_book in bookmarks[user_id]:
            await ctx.send(f"'{first_book['title']}'은(는) 이미 북마크에 추가되어 있습니다.")
        else:
            bookmarks[user_id].append(first_book)
            save_bookmarks(bookmarks)
            await ctx.send(f"'{first_book['title']}'의 정보를 북마크에 추가했습니다.")

@bot.command(name="북마크목록")
async def list_bookmarks(ctx):
    user_id = str(ctx.author.id)  # 사용자 ID
    bookmarks = load_bookmarks()  # 북마크 데이터 로드

    if user_id not in bookmarks or not bookmarks[user_id]:
        await ctx.send("현재 북마크에 저장된 책이 없습니다.")
        return

    # 북마크 데이터를 Embed와 삭제 버튼으로 출력
    for book in bookmarks[user_id]:  # 사용자 북마크 목록 순회
        embed = discord.Embed(
            title=book.get("title", "No Title"),
            url=book.get("link", ""),
            description=f"Author: {book.get('author', 'Unknown')}",
            color=0x00c3ff
        )
        if book.get("image"):
            embed.set_thumbnail(url=book["image"])

        # 삭제 버튼 추가
        view = BookmarkDeletionView(ctx, book.get("title"))
        await ctx.send(embed=embed, view=view)

@bot.command(name="도움말")
async def show_help(ctx):
    embed = discord.Embed(
        title="📚 도움말 - 명령어 목록",
        description="아래는 사용 가능한 명령어와 설명입니다:",
        color=0x00c3ff
    )

    # 명령어 목록 및 설명
    commands = {
        "!도서제목 [제목]": "입력한 제목으로 책을 검색합니다.",
        "!도서작가 [작가명]": "입력한 작가명으로 책을 검색합니다.",
        "!도서카테고리": "카테고리 선택 버튼을 제공하여 책을 검색합니다.",
        "!북마크추가 [제목]": "입력한 제목으로 책을 검색한 후 첫 번째 결과를 북마크에 추가합니다.",
        "!북마크목록": "북마크에 저장된 책 목록을 확인합니다.",
        "!도움말": "사용 가능한 명령어와 설명을 보여줍니다."
    }

    # 명령어 및 설명을 Embed에 추가
    for command, description in commands.items():
        embed.add_field(name=command, value=description, inline=False)

    await ctx.send(embed=embed)


bot.run(TOKEN)
