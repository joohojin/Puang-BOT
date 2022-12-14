import discord

bot = discord.Bot()

@bot.event
async def on_ready():
    print("{0.user}로 로그인 했어요.".format(bot))
    
@bot.slash_command(guild_ids = [1039072581237624952], description = "푸앙 제 2호 부르기")
async def talk(ctx):
    await ctx.respond("왜 부르셨습니까?")


bot.run('MTA1MjYwNTA4NDk1NTA2MjMzMw.GcgE9_.0WybHHWDSK0yPuQIChvA4WgSL9HxNKyq1sZm4w')