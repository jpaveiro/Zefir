import discord
from discord.ext import commands
from utils.consulta_utils import Consulta_Utils

class Consulta(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.tipoConsultaLista = ["ddd", "comandos"]

    @discord.slash_command(name="consulta", description="Realize uma consulta.")
    @discord.option(name="tipo_consulta", description="Tipo de consulta.")
    @discord.option(name="consulta", description="Qual deseja consultar.")
    async def consulta(self, ctx, tipo_consulta=None, consulta=None) -> None:
        tipo_consulta = tipo_consulta.lower() if tipo_consulta else None

        if (tipo_consulta == None or consulta == None or tipo_consulta not in self.tipoConsultaLista):
            embed = discord.Embed(
                title="🔍 Tipos de Consulta",
                color=0x36393F
            )
            embed.add_field(name="📱 - DDD", value="`/consulta ddd [ddd]`", inline=False)
            await ctx.respond(embed=embed)
            return
        
        match(tipo_consulta):
            case "ddd":
                embed = discord.Embed(
                    title="🛜 Consulta em andamento",
                    description=f"Consultando o DDD {consulta}...",
                    color=0x36393F
                )
                await ctx.respond(embed=embed)
                embed = discord.Embed(
                    title="📱 Consulta DDD",
                    description=f"**Response**: `{Consulta_Utils.consulta_ddd(consulta)}`",
                    color=0x36393F
                )
                embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
                await ctx.edit(embed=embed)
        
def setup(bot) -> None:
    bot.add_cog(Consulta(bot))