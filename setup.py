from distutils.core import setup

setup(
  name = 'discord.py-self_embed',
  packages = ['discord_self_embed'],
  version = '1.0.0',
  license='MIT',
  description = 'A way for selfbots to send embeds again.',
  author = 'Ben Tettmar',
  author_email = 'hello@benny.fun',
  url = 'https://github.com/bentettmar/discord.py-self_embed',
  download_url = 'https://github.com/bentettmar/discord.py-self_embed/archive/refs/tags/1.0.0.tar.gz',
  keywords = ['discord', 'embed', 'selfbot', "discord embed", "embed discord", "discord selfbot embed", "embed selfbot discord"],
  install_requires=["requests"],
  classifiers=[
    'Development Status :: 3 - Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)