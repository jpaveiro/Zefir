import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import time

tempoInicial = time.time()
load_dotenv()

bot = commands.Bot(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"[{abs(tempoInicial - time.time()):.2f}s] Sucesso ao inicializar! Logado como: {bot.user}.")
    await bot.change_presence(activity=discord.Game(name=r"Você sabia que eu sou um bot 100% brasileiro? 🤔💭"))

bot.run(os.getenv("TOKEN"))