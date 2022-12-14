import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='/', intents=intents)

game = discord.Game("열심히 학습")

intents = discord.Intents.all()

@bot.event
async def on_ready():
    print('다음으로 로그인합니다 : {0.user}'.format(bot))

# /푸앙아, /가르치기를 입력 받으면 반응

@bot.command()
async def 푸앙아(ctx):
    await ctx.reply('푸앙이는 지금 학습 중이에요! 10~20분 후에 다시 시도해주세요!')

@bot.command()
async def 가르치기(ctx):
    await ctx.reply('푸앙이는 지금 학습 중이에요! 10~20분 후에 다시 시도해주세요!')

# 상위폴더의 token.txt 파일을 읽어와 token에 저장합니다.
with open('../token.txt', 'r') as f:
    token = f.read()

bot.run(token)