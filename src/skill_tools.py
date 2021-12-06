import os, json, discord, d20
from discord.ext import commands
from src.uses_dice import UsesDice
from src.repositories.character_repository import CharacterRepository
import argparse


parser = argparse.ArgumentParser(description='Take in params for skills')
parser.add_argument('-b', "--bonus", type=int, help='Bonus die to apply to the roll')
parser.add_argument('-p', "--penalty", type=int, help='Penalty dice to apply to the roll')
parser.add_argument('option', type=str, help='A skill roll')


class SkillTools(UsesDice, commands.Cog):

  description = None
  
  
  title = "{name} is rolling {skill}"

  def __init__(self, bot):
    super().__init__()
    
    filepath = os.path.join(os.path.relpath("src/gamedata"), "characteristics.json")
    f = open(filepath, "r")
    self.characteristics_data = json.load(f)
    f.close()

    filepath = os.path.join(os.path.relpath("src/gamedata"), "skills.json")
    f = open(filepath, "r")
    self.skills_data = json.load(f)
    f.close()


  @commands.command(aliases=['a'])
  @commands.has_permissions(manage_messages=True)
  async def skill(self, ctx, *args):   
    """!skill <skill> -b <#> or -p <#>"""
    # The first arg is the skill which will throw
    # an error if passed to the parser
    parsed = parser.parse_args(args)
    skill = parsed.option

    #start by trying to figure out what skill they're rolling
    # find the skill you're comparing against
    char_repo = CharacterRepository()
    char = char_repo.get_active_character_for_user(ctx.author.id)
    
    close_skills = char.skills.get_closest_skill_name(skill)

    skill_name = await self.determine_which(ctx, close_skills)

    skill = char.skills.get_skill_by_name(skill_name)

    if not skill:
      return

    # determine bonus or penalty qty
    mod =  0 + int(parsed.bonus or 0) - int(parsed.penalty or 0)
    # A d100 is two d10s
    d100 = self.roll100( mod )

    # tell the user what they rolled
    success = skill.success_level(d100["total"])
    
    verbose_roll = f"""
    Tens: {d100["tens"]}
    Ones: {d100["ones"]}
    Results: {d100["total"]} vs {skill.val} = {"Failure" if not success else success+" Success"}"""

    embed = discord.Embed(title="Rolling", description=skill)
    embed.add_field(name=f"shake shake shake...roll.....", value=verbose_roll, inline=True)

    #await ctx.message.delete()
    await ctx.send(embed=embed)
  
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def hp(self, ctx, qty=0):
    adjusted = self.adjust_attribute( ctx, "hp_curr", qty )
    char = adjusted["char"]

    await ctx.send(f'{char.name} HP: `{adjusted["from"]} -> {adjusted["to"]}` `Max: {char.hp_max}`')
  
  @commands.command()
  async def mp(self, ctx, qty=0):
    """!mp <qty>
    Increase or reduce your current mp amount

    ex.
    !mp 3"""
    adjusted = self.adjust_attribute( ctx, "mp_curr", qty )
    char = adjusted["char"]

    await ctx.send(f'{char.name} MP: `{adjusted["from"]} -> {adjusted["to"]}/{char.mp_max}`')
  
  @commands.command()
  async def luck(self, ctx, qty=0):
    """!luck <qty>

    ex. !luck -4"""
    adjusted = self.adjust_attribute( ctx, "luck", qty )
    char = adjusted["char"]

    await ctx.send(f'{char.name} Luck: `{adjusted["from"]} -> {adjusted["to"]}`')
  
  @commands.command()
  async def san(self, ctx, qty="0"):
    """!san <qty>
    qty can be either an integer or a dice string

    !san -2
    !san -2d4"""
    roll = None
    
    if not qty.isnumeric():
      # assume its a dice string for now
      roll = d20.roll(qty)
      qty = roll.total
    else:
      qty = int(qty)

    adjusted = self.adjust_attribute( ctx, "san", qty )
    char = adjusted["char"]

    await ctx.send(f'{char.name} Sanity: `{adjusted["from"]} -> {adjusted["to"]}` `{roll or ""}`')

