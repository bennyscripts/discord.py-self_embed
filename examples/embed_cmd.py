import discord_self_embed
from discord.ext import commands

bot = commands.Bot(command_prefix=".", self_bot=True)

@bot.event
async def on_ready():
    print("ready")

@bot.command(name="embed")
async def embed_cmd(ctx):
    embed = discord_self_embed.Embed("discord.py-self_embed", description="A way for selfbots to send embeds again.", colour="ff0000", url="https://github.com/bentettmar/discord.py-self_embed")
    embed.set_author("Benny")

    await ctx.send(embed.generate_url(hide_url=True)) # You can also send the embed converted to a string which will auto hide the url.

bot.run("TOKEN_HERE")
