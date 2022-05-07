from ast import If
from nextcord.ext import commands

class Greetings(commands.Cog, name="Greetings"):
    """It send Greetings to the users"""

    def __init__(self, bot: commands.Bot):
      self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, ctx: commands.Context):

      if (ctx.author.id == self.bot.user.id):
        return

      if (ctx.content.lower().startswith(("hello", "ciao", "hi"))):
        await ctx.channel.send(f"Hi {ctx.author.mention}!")

      if (ctx.content.lower().startswith(("goodbye", "bye"))):
        await ctx.channel.send(f"Goodbye {ctx.author.mention} See you later!")
      
      if (ctx.content.lower().startswith("buongiorno")):
        await ctx.channel.send("Buongiorno un cazzo!")

def setup(bot: commands.Bot):
    bot.add_cog(Greetings(bot))