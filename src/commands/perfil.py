import discord
from discord.ext import commands

class Perfil(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="perfil", description="Veja seu perfil.")
    async def perfil(self, ctx):
        user = ctx.author
        embed = discord.Embed(
            title=f"@{user.name}",
            description="Confira seu progresso:",
            color= 0xecec53
        )
        embed.add_field(name="ID", value=user.id, inline=True)
        embed.add_field(name="Nível", value=0, inline=True)
        embed.add_field(name="Conta Zefir", value=f"$ {0:.2f}", inline=True)
        embed.set_thumbnail(url=user.avatar.url)
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Perfil(bot))