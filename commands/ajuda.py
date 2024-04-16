import discord
from discord.ext import commands

class Ajuda(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @discord.slash_command(name="ajuda", description="Veja todos os comandos disponíveis e outros.")
    async def rolardado(self, ctx) -> None:
        embed = discord.Embed(
            title="📚 Ajuda",
            description="Veja todos os comandos disponíveis e outros.",
            color=0x36393F
            )
        embed.add_field(name="🎲 Rolar Dado", value="`/rolardado [lados]`", inline=True)
        embed.add_field(name="📚 Ajuda", value="`/ajuda`", inline=True)
        embed.add_field(name="🔍 Consulta", value="`/consulta [tipo] [consulta]`", inline=True)
        await ctx.respond(embed=embed)

def setup(bot) -> None:
    bot.add_cog(Ajuda(bot))