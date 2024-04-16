import discord
from discord.ext import commands
import random
from utils.error_messages_utils import Errors_Message_Utils as error

class RolarDado(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @discord.slash_command(name="rolardado", description="Role um dado.")
    @discord.option(name="lados", description="Número de lados do dado.")
    async def rolardado(self, ctx, lados: int) -> None:
        if lados < 2:
            await ctx.respond(embed=error.rolar_dado_error(ctx, lados))
            return
        embed = discord.Embed(
            title="🎲 Temos o resultado!",
            color=0x36393F
            )
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        embed.add_field(name="↔️ Qtd de lados", value=lados, inline=True)
        embed.add_field(name="🎯 Resultado", value=random.randint(1, lados), inline=True)
        await ctx.respond(embed=embed)

def setup(bot) -> None:
    bot.add_cog(RolarDado(bot))