from interactions import Client, Message
from interactions.ext.wait_for import wait_for, setup
import asyncio

bot = Client(token="MTA1MzIwMzY3NjE1MzUyMDEyOA.Ggd2IG.wDG7Jz1h_YT3Dbdy-LChoMKC6e5Lo7Kdd9M_58")

setup(bot)

# interactions 라이브러리를 사용하여 /teach가 입력되면 가르치기 기능을 실행하도록 한다.

@bot.event()
async def on_message_create(message: Message):
    if message.content == "/teach":
        await message.channel.send("test")


# 가르치기 기능 추가
@bot.command(
    name="teach",
    description="teach me something!",
    scope=1039072581237624952,
)
async def my_second_command(ctx):
    await ctx.send("grabbing a message...")

    # A simple example check function.
    # Returns True if the original author is the same as the user invoking the wait_for.
    # Returns False if another member is attempting to invoke the wait_for
    async def check(msg):
        if int(msg.author.id) == int(ctx.author.user.id):
            return True
        await ctx.send("I wasn't asking you")
        return False

    try:
        # Define the wait_for.
        # This particular example listens for the raw on_message_create event which then returns a Message object.
        # With this, you have the ability to read the content (if the privileged intent has been
        # approved in the Discord Dev dashboard), any attachments, stickers, etc.

        answer: Message = await wait_for(ctx, "on_message_create", check=check, timeout=15)

        await ctx.send(f"You said: {answer.content}")
        # Afterwards, here you can put your code to execute after the wait_for has been fulfilled,
        # the checks have passed, and the timeout has not been reached.
    except asyncio.TimeoutError:
        # If your specified timeout reaches its end, here you may add your code for that condition.
        return await ctx.send("You said nothing :(")

# 챗봇 답변 기능 추가

@bot.command(
    name="chat",
    description="chat with me!",
)
async def my_third_command(ctx, text: str):
    await ctx.send(f"'{text}'")
    await ctx.send(f"여기에 답변 함수 입력")

bot.start()
