import interactions
import discord

bot = interactions.Client(token="MTA1MjYwNTA4NDk1NTA2MjMzMw.Gs5eON.K2N3J9QgPpV4y2NxV9vt_XH5ZsFNJf8Jz3bW8k")

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

bot.start()
