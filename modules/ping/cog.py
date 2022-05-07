from nextcord.ext import commands

class Ping(commands.Cog, name="Ping"):
    """Receive Ping Commands"""

    def __init__(self, bot: commands.Bot):
      self.bot = bot
    
    @commands.command()
    async def ping(self, ctx: commands.Context):
      """Checks if the bot is Alive"""
      await ctx.send("Pong")

def setup(bot: commands.Bot):
    bot.add_cog(Ping(bot))