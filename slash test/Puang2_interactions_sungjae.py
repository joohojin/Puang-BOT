import discord
import interactions
import asyncio

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


@bot.command(
    name = "teach",
    description = "푸앙이에게 답변 가르치기",
    scope = 1039072581237624952,
    options = [
        interactions.Option(
            name = "text",
            description = "What you want to teach",
            type = interactions.OptionType.STRING,
            required=True,
        ),
    ],
)
async def teach(ctx: interactions.CommandContext, text: str):
        # 사용자가 입력한 질문을 question에 저장합니다.
    # 받아온 question에 대한 함께 답변을 물어봅니다.
    await ctx.send("'{text}'에 대한 답변은 무엇인가요?")
    # 사용자가 입력한 답변을 받아옵니다.
    
    try:
        msg = await ctx.send('message', timeout=60.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send('시간이 초과되었습니다.')
    else:
        # 사용자가 입력한 답변을 answer에 저장합니다.
        answer = msg.content
    # 질문과 답변을 모두 불러와 추가까지 하였다면 성공적으로 추가되었다는 메시지를 출력합니다.
    await ctx.send(answer)
    

bot.start()
