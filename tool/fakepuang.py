import discord
from discord.ext import commands
import os

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

intents = discord.Intents.all() 

@bot.event
async def on_ready():
    print('다음으로 로그인합니다 : {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Game("열심히 학습"))

# /푸앙아, /가르치기를 입력 받으면 반응

# 챗봇 답변 기능
@bot.slash_command(name = "푸앙아", description = "푸앙이와 대화하기", guild_ids = [1039072581237624952])
async def teach(ctx, 메시지):
    await ctx.respond("푸앙이는 아직 학습중이에요! 10~20분 정도 기다려주세요! 금방 학습이 될거에요!")


# 가르치기 기능
@bot.slash_command(name = "가르치기", description = "푸앙이에게 질문과 대답 가르치기",guild_ids = [1039072581237624952])
async def first_command(ctx, 질문, 대답):
        await ctx.respond("푸앙이는 아직 학습중이에요! 10~20분 정도 기다려주세요! 금방 학습이 될거에요!")

# 같은폴더의 token.txt 파일을 utf-8로 읽어와서 토큰으로 사용합니다.
with open('token.txt', 'r', encoding='utf-8') as f:
        token = f.read()
    
bot.run(token)