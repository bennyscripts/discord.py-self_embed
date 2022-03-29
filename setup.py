from distutils.core import setup

readme = """
# discord.py-self_embed
A way for selfbots to send embeds again.  
It uses [Benny's embed generator](https://embed.benny.fun).

### Install
> ```bash
> $ pip install discord.py-self-embed
> ```

### Example
> ```python
> import discord_self_embed
> 
> embed = discord_self_embed.Embed("discord.py-self_embed", 
>   description="A way for selfbots to send embeds again.", 
>   colour="ff0000", 
>   url="https://github.com/bentettmar/discord.py-self_embed"
> )
> embed.set_author("Ben Tettmar")
> 
> url = embed.generate_url(hide_url=True) # You can also convert the embed to a string.
> print(url) # The url will be put in your ctx.send() content.
> ```

### Limitations
> Because the embeds are web embeds there are limitations.  
> - No footers.
> - Max 350 character description.

"""

setup(
    name='discord.py-self_embed',
    packages=['discord_self_embed', 'discord_self_embed.utils'],
    version='1.0.5',
    license='MIT',
    description='A way for selfbots to send embeds again.',
    author='Ben Tettmar',
    author_email='hello@benny.fun',
    url='https://github.com/bentettmar/discord.py-self_embed',
    download_url='https://github.com/bentettmar/discord.py-self_embed/archive/refs/tags/1.0.5.tar.gz',
    keywords=['discord', 'embed', 'selfbot', "discord embed",
              "embed discord", "discord selfbot embed", "embed selfbot discord"],
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    long_description=readme,
    long_description_content_type='text/markdown'
)
