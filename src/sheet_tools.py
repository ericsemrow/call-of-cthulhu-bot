import discord
from discord.ext import commands
from src.repositories.google_sheets import GoogleSheets
from src.repositories.character_repository import CharacterRepository

class SheetTools(commands.Cog):
  
  @commands.command()
  async def gsheet(self, ctx, arg):
    g_sheets = GoogleSheets()
    char_repo = CharacterRepository()
    sheet_id = g_sheets.get_sheet_id(arg)
    sheet_data = g_sheets.get_sheet_by_id(sheet_id)
    char = char_repo.get_char_from_raw(sheet_data)
    char.owner = ctx.author.id
    char_repo.store_character_for_user(char, ctx.author.id)
  
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def sheet(self, ctx):
    char_repo = CharacterRepository()
    char = char_repo.get_active_character_for_user(ctx.author.id)

    if char is not None:
      await ctx.message.delete()
      await ctx.send(embed=char_repo.getEmbed(ctx, char))
    else:
      await self.handle_no_sheet(ctx)
    
 
  async def handle_no_sheet(self, ctx):
    ctx.send("No sheet loaded. Have you used `!sheet <url>`?")

  