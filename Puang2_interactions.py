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

bot.start()
