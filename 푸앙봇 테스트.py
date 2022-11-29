import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import youtube_dl
import asyncio
import nacl

game = discord.Game("퐝퐝이") 

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='푸앙아 ', status=discord.Status.online, activity=game, intents=intents)

@bot.event
async def on_ready():
    print('다음으로 로그인합니다 : {0.user}'.format(bot))

@bot.command()
async def Hello(ctx):
    await ctx.send("안녕하세요!")

#data.txt를 uft-8로 읽어서 data에 저장합니다
with open("data.txt", "r", encoding="utf-8") as f:
    data = f.read()

@bot.command()
async def 푸앙이(ctx):
    await ctx.send(data)

@bot.command()
async def ㅁㄴㅇㄹ(ctx):
    await ctx.send("/역할 요청하기 역할:@1분반")

@bot.command()
async def 애옹(ctx):
    await ctx.send("https://media.discordapp.net/attachments/844584876904677440/895539776709607454/95261-20211007-140653-000.gif")

@bot.command()
async def 멈머이(ctx):
    await ctx.send("https://media.discordapp.net/attachments/1039072581237624957/1044436169804484658/629b065f07bd59226785164e6a2310f1.gif")

@bot.command()
async def 단수(ctx):
    await ctx.send("https://media.discordapp.net/attachments/1039072581237624957/1044436780654547094/SneakyUnfortunateHermitcrab-size_restricted.gif")

@bot.command()
async def 들어와(ctx):
    if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send("자 드가자~")
    else:
        await ctx.send("음성 채널에 먼저 들어가주세요!")
"""
@bot.command()
async def 노래틀어줘(ctx, url):
    channel = ctx.author.voice.channel
    if bot.voice_clients != []:
        await ctx.send("둠칫 두둠칫! " + str(bot.voice_clients[0].channel) + "번 방에 연결되었습니다!")

        ydl_opts = {'format': 'bestaudio'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            URL = info['formats'][0]['url']
        voice = bot.voice_clients[0]
        voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
    else:
        await channel.connect()
        await ctx.send("둠칫 두둠칫! " + str(bot.voice_clients[0].channel) + "번 방에 연결되었습니다!")

        ydl_opts = {'format': 'bestaudio'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            URL = info['formats'][0]['url']
        voice = bot.voice_clients[0]
        voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
"""

"""       
@bot.command()
async def 유튜브검색(ctx, *, search):
    channel = ctx.author.voice.channel
    if bot.voice_clients == []:
        await channel.connect()
        await ctx.send("둠칫 두둠칫! " + str(bot.voice_clients[0].channel) + "번 방에 연결되었습니다!")

        ydl_opts = {'format': 'bestaudio'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info("ytsearch:" + search, download=False)
            URL = info['entries'][0]['formats'][0]['url']
        voice = bot.voice_clients[0]
        voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
"""

@bot.command()
async def 노래틀어줘(ctx, *, search):
    channel = ctx.author.voice.channel
    if bot.voice_clients != []:
        await ctx.send("둠칫 두둠칫! " + str(bot.voice_clients[0].channel) + "번 방에 연결되었습니다!")

        ydl_opts = {'format': 'bestaudio'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info("ytsearch:" + search, download=False)
            URL = info['entries'][0]['formats'][0]['url']
        voice = bot.voice_clients[0]
        voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
    else:
        await channel.connect()
        await ctx.send("둠칫 두둠칫! " + str(bot.voice_clients[0].channel) + "번 방에 연결되었습니다!")

        ydl_opts = {'format': 'bestaudio'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info("ytsearch:" + search, download=False)
            URL = info['entries'][0]['formats'][0]['url']
        voice = bot.voice_clients[0]
        voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
    await ctx.send("지금 틀고 있는 노래는 " + info['entries'][0]['title'] + "입니다!")
        
@bot.command()
async def 일시정지(ctx):
    if not bot.voice_clients[0].is_paused():
        bot.voice_clients[0].pause()
        await ctx.send("일시정지!")
    else:
        await ctx.send("이미 일시정지 되어있어요!")

@bot.command()
async def 재생(ctx):
    if bot.voice_clients[0].is_paused():
        bot.voice_clients[0].resume()
        await ctx.send("재생!")
    else:
        await ctx.send("이미 재생중이에요!")

@bot.command()
async def 정지(ctx):
    if bot.voice_clients[0].is_playing():
        bot.voice_clients[0].stop()
        await ctx.send("정지!")
    else:
        await ctx.send("아무것도 재생중이지 않아요!")

# 봇이 퇴장할 수 있도록 하는 명령어
@bot.command()
async def 나가(ctx):
    if bot.voice_clients != []:
        await bot.voice_clients[0].disconnect()
        await ctx.send("흐잉...")
    else:
        await ctx.send("저는 아직 아무 채널에도 들어가있지 않아요!")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Ah, 잘 알아두세요. 그런건 읎어요.")

bot.run('여기에 토큰 입력')