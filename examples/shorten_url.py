import discord_self_embed

shortener = discord_self_embed.utils.Shortener("YOUR_BITLY_API_TOKEN")

embed = discord_self_embed.Embed("discord.py-self_embed", description="A way for selfbots to send embeds again.", colour="ff0000", url="https://github.com/bentettmar/discord.py-self_embed")
embed.set_author("Benny")

url = embed.generate_url(shorten_url=True, shortener=shortener)
print(url)