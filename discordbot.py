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
        msg = "안내봇 테스트중... <@813959563584864266>"
        channel = client.get_channel(1098618958795526224)
        await channel.send(msg)

    if message.content == f'{PREFIX}미인증공지' :
        msg = "<@&1098618958740987915> 
뉴라이프 | NewLife 입국 [인증] 양식입니다.

=========================================
로블록스 닉네임 : 
로블록스 프로필링크 : 
인벤토리를 오픈했나요: [O/X]
그룹 가입 인증사진 : 
=========================================

어렵지 않은 간단한 양식이니, 이 양식에 따라서 입국심사 [인증] 해주시면 감사하겠습니다.
-뉴라이프 관리진 일동-"
        channel = client.get_channel(1098618960007671827)
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
