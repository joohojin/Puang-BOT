import discord
from discord import app_commands

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name = "hi",description="푸앙봇 제 2호와 인사하기", guild=discord.Object(id = 1039072581237624952))
async def first_command(interaction):
    await interaction.response.send_message("Hello!")

@tree.command(name = "teach", description = "학습하기", guild = discord.Object(id = 1039072581237624952))
async def second_command(interaction):
    await interaction.response.send_message("뭐")
    
@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id = 1039072581237624952))
    print("{0.user}로 로그인합니다.")

client.run('토큰')