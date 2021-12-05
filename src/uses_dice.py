import d20
import discord
from src.repositories.character_repository import CharacterRepository

class UsesDice(object):

  def adjust_attribute( self, ctx, attr, qty ):
    char_repo = CharacterRepository()
    char = char_repo.get_active_character_for_user(ctx.author.id)

    try:
      old_val = getattr(char,attr)
      new_val = old_val + int(qty)
      setattr(char, attr, new_val)

      char_repo.store_character_for_user(char, ctx.author.id)
    except KeyError:
      return
    
    return {
      "char":char,
      "from": old_val,
      "to": new_val
    }
 
  def roll100(self, mod:int=0):
    num_die = 1+abs(mod)
    keep =  "" if num_die == 0 else "kl1" if num_die > 0 else "kh1"
    tens = d20.roll( f'{num_die}d10{keep}-1' )
    ones = d20.roll( "1d10-1" )

    return {
      "tens": tens,
      "ones": ones,
      "total": int(f'{str(tens.total)}{str(ones.total)}')
    }


  async def determine_which(self, ctx, options):
    if not len(options):
      # can't find anything close
      await ctx.send("No matching skill")

      return
    elif len(options) > 1:
      # well now we have too many options
      query_msg = """More than one option matches your request.

      reply"""
      for i in range(len(options)):
        query_msg += f"""
        {i+1}: {options[i]}"""

      channel = ctx.message.channel
      def check(m):
        return m.content.isnumeric and m.channel == channel

      await ctx.send(query_msg)
      msg = await ctx.bot.wait_for("message", check=check, timeout=30)
      
      name = options[int(msg.content) - 1]
    else:
      name = options[0]
      
    return name