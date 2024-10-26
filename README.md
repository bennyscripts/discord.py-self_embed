# discord.py-self_embed
A way for selfbots to send embeds again.  
It uses [Benny's Embed Generator](https://benny.fun/embed).


### Install
> ```bash
> $ pip install 'discord.py-self_embed @ git+https://github.com/bentettmar/discord.py-self_embed'
> ```

### Example
> ```python
> import discord_self_embed
> 
> embed = discord_self_embed.Embed("discord.py-self_embed", 
>   description="A way for selfbots to send embeds again.", 
>   colour="FFBB00"
> )
> embed.set_author("Benny")
> embed.set_image("https://raw.githubusercontent.com/bennyscripts/ghost/refs/heads/main/ghost.png", big=False)
> 
> url = embed.generate_url(hide_url=True) # You can also convert the embed to a string.
> print(url) # The url will be put in your ctx.send() content.
> ```

### Limitations
> Because the embeds are web embeds there are limitations.  
> - No footers.
> - Max 350 character description.
