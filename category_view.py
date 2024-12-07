import discord
from discord.ui import View, Button
from book_search import search_book_by_title  # 도서 검색 함수 가져오기

# 카테고리 선택 View 정의
class CategorySelectionView(View):
    def __init__(self, ctx, categories):
        super().__init__()
        self.ctx = ctx  # 명령어를 호출한 사용자 컨텍스트
        
        # 카테고리 버튼 추가
        for category in categories:
            self.add_item(CategoryButton(category, ctx))

# 카테고리 버튼 정의
class CategoryButton(Button):
    def __init__(self, category, ctx):
        super().__init__(label=category, style=discord.ButtonStyle.primary)
        self.category = category
        self.ctx = ctx  # ctx를 버튼으로 전달

    async def callback(self, interaction: discord.Interaction):
        try:
            # 상호작용 응답 처리 (Deferred 상태 설정)
            await interaction.response.defer()

            # 버튼 클릭 이벤트 처리
            books = search_book_by_title(self.category)
            
            if isinstance(books, str):  # 검색 결과 없음
                await interaction.followup.send(books, ephemeral=True)
            else:
                # Embed 리스트 생성
                embeds = []
                for book in books[:5]:  # 상위 5개 결과만 표시
                    embed = discord.Embed(
                        title=book.get("title", "No Title"),
                        url=book.get("link", ""),
                        description=f"Author: {book.get('author', 'Unknown')}",
                        color=0x00c3ff
                    )
                    if book.get("image"):
                        embed.set_thumbnail(url=book["image"])
                    embeds.append(embed)

                # 모든 Embed를 하나의 메시지로 전송
                await interaction.followup.send(embeds=embeds)

        except Exception as e:
            # 예외 처리
            error_message = f"오류가 발생했습니다: {str(e)}"
            await interaction.followup.send(error_message, ephemeral=True)
