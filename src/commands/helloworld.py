import discord
from discord.ext import commands

class HelloWorld(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="helloworld", description="Primeiro comando.")
    async def helloworld(self, ctx):
        await ctx.respond("Hello World!")

def setup(bot):
    bot.add_cog(HelloWorld(bot))