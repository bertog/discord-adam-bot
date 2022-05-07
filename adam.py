import os
from dotenv.main import load_dotenv
from nextcord.ext import commands

def main():

	client = commands.Bot(command_prefix="!")

	load_dotenv()

	@client.event
	async def on_ready():
		print(f"{client.user.name} has connected to discord")

	@client.event
	async def on_message(ctx):
		if (ctx.content.startswith("Hello")):
			await ctx.channel.send(f"Hi {ctx.author.mention}!")

		await client.process_commands(ctx)

	@client.command()
	async def ping(ctx):
		"""Checks if the bot is Alive"""
		await ctx.send("Pong")

	client.run(os.getenv("DISCORD_TOKEN"))

if __name__ == '__main__':
	main()
  