import discord
import interactions

bot = interactions.Client(token="토큰")

@bot.command(
    name="say_something",
    description="say something!",
    scope=1039072581237624952,
    options = [
        interactions.Option(
            name="text",
            description="What you want to say",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ],
)
async def my_first_command(ctx: interactions.CommandContext, text: str):
    await ctx.send(f"You said '{text}'!")

# 가르치기 기능 추가
@bot.command(
    name="teach",
    description="teach me something!",
    scope=1039072581237624952,
)
async def my_second_command(ctx: interactions.CommandContext):
    await ctx.send(f"가르쳐드릴게요!")
    await teach_command(ctx)


# my_second_command에서 사용할 수 있는 학습 명령어를 추가합니다.

def teach_command(text: str):
    @bot.command()
    async def asdf(ctx):
        # 사용자 입력을 받아 question에 저장합니다. 제한시간은 30초입니다.
        await ctx.send("질문?")
        question = await ctx.wait_for_input(timeout=30)
        # 사용자 입력을 받아 answer에 저장합니다.
        await ctx.send("답변?")
        answer = await ctx.wait_for_input(timeout=30)
        
        # question과 answer를 출력합니다.
        await ctx.send(f"질문: {question}")
        await ctx.send(f"답변: {answer}")

# 챗봇 답변 기능 추가

@bot.command(
    name="chat",
    description="chat with me!",
    scope=1039072581237624952,
    options = [
        interactions.Option(
            name="text",
            description="What you want to say",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ],
)
async def my_third_command(ctx: interactions.CommandContext, text: str):
    await ctx.send(f"'{text}'")
    await ctx.send(f"여기에 답변 함수 입력")

bot.start()
