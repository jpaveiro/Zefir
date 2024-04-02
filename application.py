import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import time
from utils.mongodb_utils import MongoDB_Utils as Utils
import datetime

load_dotenv()
bot = commands.Bot(intents=discord.Intents.all())
InitialTime = time.time()
utils = Utils()

@bot.event
async def on_ready():
    print(f"[{abs(InitialTime - time.time()):.2f}s] Sucesso ao inicializar! Logado como: {bot.user}.")
    await bot.change_presence(activity=discord.Game(name=r"Você sabia que eu sou um bot 100% brasileiro? 🤔💭"))

@bot.before_invoke
async def before_invoke(ctx):
    print(f"[{datetime.datetime.now().strftime("%Y-%m-%d | %H:%M:%S")}] Comando {ctx.command} foi invocado por {ctx.author}.")
    await utils.register_if_not_exists(ctx.author.id)

not_load = [""]
for filename in os.listdir("commands/"):
    if filename.endswith(".py") and filename not in not_load:
        bot.load_extension(f"commands.{filename[:-3]}")

def run():
    bot.run(os.getenv("TOKEN"))

if (__name__ == "__main__"):
    run()