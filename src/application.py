import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import time
import asyncio

class ZefirBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.InitialTime = time.time()
        load_dotenv()
        self.not_load = [""]
        for filename in os.listdir("src/commands/"):
            if filename.endswith(".py") and filename not in self.not_load:
                self.load_extension(f"src.commands.{filename[:-3]}")

    async def on_ready(self):
        print(f"[{abs(self.InitialTime - time.time()):.2f}s] Sucesso ao inicializar! Logado como: {self.user}.")
        await self.change_presence(activity=discord.Game(name=r"Você sabia que eu sou um bot 100% brasileiro? 🤔💭"))

    def run_bot():
        bot = ZefirBot(intents=discord.Intents.all())
        asyncio.run(bot.run(os.getenv("TOKEN")))

if __name__ == "__main__":
    ZefirBot.run_bot()