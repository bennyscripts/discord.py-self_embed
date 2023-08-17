# discord.py-self_embed
A way for selfbots to send embeds again.  
It uses [Rauf's embed generator](https://embed.rauf.wtf/).

## Reason for archive
Unfortunatly, the creator of Rauf's embed generator (Rauf) has made the decision to close the embed generator. This means that this library will become unusable.
![CleanShot 2023-08-17 at 9 25 50@2x](https://github.com/bennyscripts/discord.py-self_embed/assets/83777519/5c5f719f-2185-40b5-88ca-893d2593e0f1)


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
>   colour="ff0000"
> )
> embed.set_author("Benny")
> 
> url = embed.generate_url(hide_url=True) # You can also convert the embed to a string.
> print(url) # The url will be put in your ctx.send() content.
> ```

### Limitations
> Because the embeds are web embeds there are limitations.  
> - No footers.
> - Max 350 character description.
