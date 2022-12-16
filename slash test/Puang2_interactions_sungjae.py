import discord
import interactions
import asyncio

bot = interactions.Client(token="토큰")

user_dic = {}

@bot.command(
    name = "teach", #/명령어 이름
    description = "teaching Puang", #/명령어 설명
    scope = 1039072581237624952, #서버 id
    options = [
        interactions.Option(
            name = "question", #/명령어 옵션 이름
            description = "What question do you want to teach", #/명령어 옵션 설명
            type = interactions.OptionType.STRING,
            required=True,
        ),
        interactions.Option(
            name = "answer",
            description = "what answer do you want to teach",
            type = interactions.OptionType.STRING,
            required = True, 
        ),
    ],
)
async def first_command(ctx: interactions.CommandContext, question, answer):
        await ctx.send(f"You teach the question: ``'{question}'``")
        await ctx.send(f"You teach the answer: ``'{answer}'`` to the question: ``'{question}'``")
        



bot.start()
