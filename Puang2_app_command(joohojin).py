import discord
from discord import app_commands

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name = "hi",description="푸앙봇 제 2호와 인사하기", guild=discord.Object(id = 1039072581237624952))
async def first_command(interaction):
    await interaction.response.send_message("Hello!")

# 학습하기
@tree.command(name = "teach", description = "학습하기", guild = discord.Object(id = 1039072581237624952))
async def second_command(interaction):
    # 사용자의 입력을 받는다.
    await interaction.response.send_message("뭐")
    question = await client.wait_for('message', check=lambda message: message.author == interaction.user)
    await interaction.response.send_message("뭐라고?")
    answer = await client.wait_for('message', check=lambda message: message.author == interaction.user)
    await interaction.response.send_message("알겠어")
    # 질문과 답변을 전송한다.
    await interaction.response.send_message("질문: " + question.content + "답변: " + answer.content)

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id = 1039072581237624952))
    print("{0.user}로 로그인합니다.")

client.run('토큰')