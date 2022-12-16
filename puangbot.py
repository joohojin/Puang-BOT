import interactions
import asyncio
import os
import pandas as pd
import time

import datetime

bot = interactions.Client(token="토큰")

user_dic = {}

with open("data/puang-art.txt", "r", encoding="utf-8") as f:
    data = f.read()

'''
# 이스터에그
@bot.command()
async def 푸앙이(ctx):
    await ctx.send(data)

@bot.command()
async def 애옹(ctx):
    await ctx.send("https://media.discordapp.net/attachments/844584876904677440/895539776709607454/95261-20211007-140653-000.gif")
'''

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


# 챗봇 답변 기능
@bot.command(
    name="chat",
    description="chatbot",
    scope=1039072581237624952,
    options=[
        interactions.Option(
            name="question",
            description="please ask me a question",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ],
)
async def teach(ctx: interactions.CommandContext, question):
    await ctx.send(question)


# 가르치기 기능
@bot.command(
    name = "teach", #/명령어 이름
    description = "teach me!", #/명령어 설명
    scope = 1039072581237624952, #서버 id
    options = [
        interactions.Option(
            name = "question:", #/명령어 옵션 이름
            description = "what do you want to ask?", #/명령어 옵션 설명
            type = interactions.OptionType.STRING,
            required=True,
        ),
        interactions.Option(
            name = "answer:", #/명령어 옵션 이름
            description = "what do you want to answer?", #/명령어 옵션 설명
            type = interactions.OptionType.STRING,
            required = True, 
        ),
    ],
)
async def first_command(ctx: interactions.CommandContext, question, answer):
        await ctx.send(f"``'{answer}'````'{question}'``")

        # 질문과 답변을 저장
        today = datetime.datetime.today()
        today = today.strftime("%Y-%m-%d")
        chatbot_data.loc[len(chatbot_data)] = [question, answer, today + "(" + ctx.author.name + ")"]
        # ChatBotData.csv를 저장합니다.
        chatbot_data.to_csv('data/ChatBotData.csv', index=False)


# 먼저 기존의 ChatBotData.csv를 data\ChatBotData-Old에 저장합니다.
save_old_chatbot_data()

# 만약 data\ChatBotData-Old에 백업 csv 파일이 10개를 초과하면 만들어진 날짜가 가장 오래된 백업 csv파일을 삭제합니다.
delete_old_chatbot_data()


bot.start()












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