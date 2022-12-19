import discord
from discord.ext import commands
from discord.commands import Option

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='^^', intents = intents)

@bot.event
async def on_ready():
    print("{0.user} online.")
    
@bot.slash_command(guild_ids = [1039072581237624952], name = "푸앙 제 2호", description = "푸앙 제 2호와 인사하기")
async def teach2(ctx, 메시지:Option("할 말 입력")):
    await ctx.respond(ctx.author.name +  "님 :" + 메시지)
    
bot.run('토큰')