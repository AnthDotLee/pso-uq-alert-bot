import os

import discord
from discord.utils import get

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


async def post_to_channel(message):
    guild = client.guilds[0]
    channel = get(guild.channels, name='more-gaems', type=discord.ChannelType.text)
    await channel.send(message)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await post_to_channel('Hi Hello!')

client.run(TOKEN)