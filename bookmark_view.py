import discord
from discord.ui import View, Button
from bookmark_manager import load_bookmarks, save_bookmarks

# 북마크 삭제 버튼 View 정의
class BookmarkDeletionView(View):
    def __init__(self, ctx, book_title):
        super().__init__()
        self.ctx = ctx
        self.book_title = book_title
        self.add_item(BookmarkDeleteButton(book_title, ctx))

class BookmarkDeleteButton(Button):
    def __init__(self, book_title, ctx):
        super().__init__(label=f"삭제: {book_title}", style=discord.ButtonStyle.danger)
        self.book_title = book_title
        self.ctx = ctx

    async def callback(self, interaction: discord.Interaction):
        user_id = str(self.ctx.author.id)
        bookmarks = load_bookmarks()

        if user_id not in bookmarks or self.book_title not in [book.get("title") for book in bookmarks[user_id]]:
            await interaction.response.send_message(f"'{self.book_title}'은(는) 북마크에 없습니다.", ephemeral=True)
        else:
            # 해당 제목을 가진 책 제거
            bookmarks[user_id] = [book for book in bookmarks[user_id] if book.get("title") != self.book_title]
            save_bookmarks(bookmarks)
            await interaction.response.send_message(f"'{self.book_title}'을(를) 북마크에서 삭제했습니다.", ephemeral=True)
