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
        msg = "@everyone 서버가 오픈되었습니다! 서버를 즐겨보세요! 게임 접속 : https://www.roblox.com/games/13350091161/NewLife#!/game-instances"
        channel = client.get_channel(1098618958795526224)
        await channel.send(msg)

    if message.content == f'{PREFIX}서버닫음' :
        msg = "서버가 닫혔습니다! 다음 오픈을 기대해 주세요!"
        channel = client.get_channel(1098618958795526224)
        await channel.send(msg)

    if message.content == f'{PREFIX}점검실시' :
        msg = ":tools: 안내봇 점검 및 테스트중입니다! 이용에 착오없으시길 바랍니다."
        channel = client.get_channel(1098618958795526224)
        await channel.send(msg)

    if message.content == f'{PREFIX}점검완료' :
        msg = ":white_check_mark: 안내봇 점검이 종료되었습니다!"
        channel = client.get_channel(1098618958795526224)
        await channel.send(msg)

@client.event
async def on_member_join(member) :
    msg = "안녕하세요! 뉴라이프에 오신것을 환영합니다!"
    channel = client.get_channel(1098618960297087050)
    await channel.send(msg)

try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
