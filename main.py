import os
import keepalive
from discord.ext import commands
from src.skill_tools import SkillTools
from src.sheet_tools import SheetTools
from src.helpers import Helpers


bot = commands.Bot(command_prefix='!')

@bot.listen('on_ready')
async def is_ready():
    print("Online")


bot.add_cog(SkillTools(bot))
bot.add_cog(SheetTools(bot))
bot.add_cog(Helpers(bot))


keepalive.keep_alive()
token = os.environ.get("DISCORD_TOKEN") 
bot.run(token)