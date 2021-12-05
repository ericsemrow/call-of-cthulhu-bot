from discord.ext import commands
import d20
import argparse


parser = argparse.ArgumentParser(description='Take in params')
parser.add_argument('-b', "--bonus", type=int, help='Bonus die to apply to the roll')
parser.add_argument('-p', "--penalty", type=int, help='Penalty dice to apply to the roll')



class Helpers(commands.Cog):
  @commands.command(aliases=['r'])
  @commands.has_permissions(send_messages=True)
  async def roll(self, ctx, *, arg):
    """Standard dice roller. Alias: r"""
    await ctx.send(str(d20.roll(arg)))

  

  @roll.error
  async def handle_bot_exceptions(self, ctx, error):
    if isinstance(error, commands.MissingPermissions):
      await ctx.send("This bot seems to be missing the required permissions.")
    if isinstance(error, commands.CommandInvokeError):
      await ctx.send("This bot seems to be missing the required permission.")