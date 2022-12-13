# 챗봇 실시간 구현

# Commented out IPython magic to ensure Python compatibility.
# %pip install schedule

# 디스코드 챗봇 구현

import discord
from discord import app_commands
from discord import Interaction
from discord.ext import commands
from discord.ext.commands import Bot
import os
import pandas as pd
import time

import datetime

game = discord.Game("퐝퐝이") 

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='푸앙아 ', status=discord.Status.online, activity=game, intents=intents)

@bot.event
async def on_ready():
    print('다음으로 로그인합니다 : {0.user}'.format(bot))

with open("data/puang-art.txt", "r", encoding="utf-8") as f:
    data = f.read()


# 이스터에그
@bot.command()
async def 푸앙이(ctx):
    await ctx.send(data)

@bot.command()
async def 애옹(ctx):
    await ctx.send("https://media.discordapp.net/attachments/844584876904677440/895539776709607454/95261-20211007-140653-000.gif")

# 챗봇
@bot.slash_command(ctx, name = '푸앙아', description = '푸앙이와 대화하기')
async def 대화(interaction : Interaction, *, message : str):  
    # 푸앙 메시지를 입력하면 chat(메시지) 함수를 출력합니다.
    # 이제 답장으로 푸앙이가 말할 수 있게 되었습니다.
    await interaction.reply(chat(message))

# 명령어가 없을 때
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("그런 명령어는 존재하지 않아요!")



# 데이터 학습 및 저장 구현

# 기존의 ChatBotData.csv 파일을 읽어온다.
chatbot_data = pd.read_csv('data/ChatBotData.csv')



# data\ChatBotData-Old에 ChatBotData.csv의 이름을 ChatBotData(오늘의 날짜 및 시간).csv로 변경하여 저장해주는 함수
def save_old_chatbot_data():
    today = datetime.datetime.today()
    today = today.strftime("%Y-%m-%d-%H-%M-%S")
    chatbot_data.to_csv('data/ChatBotData-Old/ChatBotData({}).csv'.format(today), index=False)

# 만약 data\ChatBotData-Old에 백업 csv 파일이 10개를 초과하면 만들어진 날짜가 가장 오래된 백업 csv파일을 삭제하는 함수
def delete_old_chatbot_data():
    file_list = os.listdir('data/ChatBotData-Old')
    if len(file_list) > 10:
        # len(file_list) - 10은 백업 csv 파일이 10개를 초과하는 만큼의 숫자
        for i in range(len(file_list) - 10):
            # 백업 csv 파일이 만들어진 날짜가 가장 오래된 파일을 삭제
            os.remove('data/ChatBotData-Old/' + file_list[i])




# 챗봇에게 질문과 답변을 가르치는 함수
@bot.slash_command(ctx, name = '가르치기', description = "푸앙이에게 답변 가르치기")
async def 가르치기(interaction: Interaction):
    # 먼저 디스코드 사용자에게 질문을 채팅으로 물어봅니다.
    await interaction.send("뭐라고 물어보실 건가요?")
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






# main부분

# Commented out IPython magic to ensure Python compatibility.
# Jupyter Notebook에서는 이 코드를 실행하세요
# %pip install nest_asyncio 
import nest_asyncio 
nest_asyncio.apply()

# 먼저 기존의 ChatBotData.csv를 data\ChatBotData-Old에 저장합니다.
save_old_chatbot_data()

# 만약 data\ChatBotData-Old에 백업 csv 파일이 10개를 초과하면 만들어진 날짜가 가장 오래된 백업 csv파일을 삭제합니다.
delete_old_chatbot_data()

bot.run('여기에 토큰 입력')











# 주의! 다음 코드는 ChatBotData.csv의 빠른 복구를 위한 코드입니다.

'''
# 기존의 data\ChatBotData-Old\ChatBotData.csv를 읽어와 data\ChatBotData.csv에 저장합니다. 데이터를 복구하시겠습니까? 라는 질문에 사용자가 y를 입력하면 복구합니다.
def restore_old_chatbot_data():
    chatbot_data = pd.read_csv('data/ChatBotData-Old/Default/ChatBotData.csv')
    chatbot_data.to_csv('data/ChatBotData.csv', index=False)
    print("기존의 ChatBotData.csv가 복구되었습니다.")

# 복구할지 물어봅니다.
print("데이터를 복구하시겠습니까?")
answer = input("y/n : ")
if answer == "y":
    # 한 번 더 물어봅니다.
    print("진짜?")
    answer = input("y/n : ")
    if answer == "y":
        print("정말로?")
        answer = input("y/n : ")
        if answer == "y":
            print("사실 복구하기 싫죠?")
            answer = input("y/n : ")
            if answer == "y":
                print("그럼 복구하지 않겠습니다.")
            else:
                restore_old_chatbot_data()
        else:
            print("데이터 복구를 취소하였습니다.")
    else:
        print("데이터 복구를 취소하였습니다.")     
else:
    print("데이터 복구를 취소하였습니다.")
'''