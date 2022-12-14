import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import asyncio
import nacl

bot = discord.Bot()

@bot.event
async def on_ready():
    print("{0.user}로 로그인 했어요.".format(bot))
    

# 챗봇
@bot.slash_command(guild_ids = [1039072581237624952], description = '푸앙이와 대화하기')
async def 푸앙제2호(ctx, *, message):
    # 푸앙 메시지를 입력하면 chat(메시지) 함수를 출력합니다.
    # 이제 답장으로 푸앙이가 말할 수 있게 되었습니다.
    await ctx.reply(chat(message))


# 명령어가 없을 때
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("그런 명령어는 존재하지 않아요!")
        
        
# 챗봇에게 질문과 답변을 가르치는 함수
@bot.slash_command(guild_ids = [1039072581237624952],description = '푸앙이에게 답변 가르치기')
async def 가르치기(ctx):
    # 먼저 디스코드 사용자에게 질문을 채팅으로 물어봅니다.
    await ctx.send("뭐라고 물어보실 건가요?")
    # 사용자가 채팅으로 답변을 입력할 때까지 기다립니다.
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        msg = await bot.wait_for('message', timeout=60.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send('시간이 초과되었습니다.')
    else:
        # 사용자가 입력한 질문을 question에 저장합니다.
        question = msg.content
    # 받아온 question에 대한 함께 답변을 물어봅니다.
    await ctx.send(question + "에 대한 답변은 무엇인가요?")
    # 사용자가 입력한 답변을 받아옵니다.
    
    try:
        msg = await bot.wait_for('message', timeout=60.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send('시간이 초과되었습니다.')
    else:
        # 사용자가 입력한 답변을 answer에 저장합니다.
        answer = msg.content
    # 받아온 질문과 답변을 quastion,answer,날짜(사용자이름) 으로ChatBotData.csv에 추가합니다.
    today = datetime.datetime.today()
    today = today.strftime("%Y-%m-%d")
    chatbot_data.loc[len(chatbot_data)] = [question, answer, today + "(" + ctx.author.name + ")"]
    # ChatBotData.csv를 저장합니다.
    chatbot_data.to_csv('data/ChatBotData.csv', index=False)
    # 질문과 답변을 모두 불러와 추가까지 하였다면 성공적으로 추가되었다는 메시지를 출력합니다.
    await ctx.send("질문과 답변이 추가되었습니다!")
    
    
bot.run('MTA1MjYwNTA4NDk1NTA2MjMzMw.GcgE9_.0WybHHWDSK0yPuQIChvA4WgSL9HxNKyq1sZm4w')