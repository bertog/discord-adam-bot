from nextcord.ext import commands
import random

class Choice(commands.Cog, name="Choice"):
    """Help users in their choise with Bot opinions"""

    def __init__(self, bot: commands.Bot):
      self.bot = bot
    
    @commands.command()
    async def choose(self, ctx: commands.Context, *args):
      """It choose from the choise provided by the user"""
      choise = random.choice(args)
      await ctx.send(choise)
    
    @commands.command()
    async def opinion(self, ctx: commands.Context):
      """It give his opinion on a question that request a Yes/No answer"""
      replies = ("Yes", "No", "Dunno", "I don't give a shit")
      await ctx.send(random.choice(replies))

def setup(bot: commands.Bot):
    bot.add_cog(Choice(bot))