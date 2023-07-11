from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
intents = discord.Intents.all()
intents.members = True
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == f'{PREFIX}call':
        await message.channel.send("callback!")

    if message.content.startswith(f'{PREFIX}hello'):
        await message.channel.send('Hello!')

    if message.content == f'{PREFIX}서버오픈' :
        svop = "안내봇 테스트중... @subway_kr"
        channel = bot.get_channel('1098618958795526224')
        await channel.send(svop)

@client.event
async def on_member_join(member) :
    msg = "안녕하세요! 뉴라이프에 오신것을 환영합니다!"
    channel = bot.get_channel('1098618960297087050')
    await channel.send(msg)

try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
