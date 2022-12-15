import discord
from discord import app_commands

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name = "hi",description="푸앙봇 제 2호와 인사하기", guild=discord.Object(id = 1039072581237624952))
async def first_command(interaction):
    await interaction.response.send_message("Hello!")

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id = 1039072581237624952))
    print("{0.user}로 로그인합니다.")

client.run('MTA1MjYwNTA4NDk1NTA2MjMzMw.GEcnT9.lHPvQdJbslviBY9uUl3dZS5e7196jbEcsMsuKc')