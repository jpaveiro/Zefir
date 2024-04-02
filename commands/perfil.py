import discord
from discord.ext import commands
from utils.mongodb_utils import MongoDB_Utils

class Perfil(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.utils = MongoDB_Utils()

    @discord.slash_command(name="perfil", description="Veja seu perfil.")
    async def perfil(self, ctx):
        user = ctx.author

        await self.utils.register_if_not_exists(user.id)
        response = self.utils.fetch_user_by_id(user.id)

        embed = discord.Embed(
            title=f"@{user.name}",
            description="Confira seu progresso:",
            color= 0xecec53
        )
        embed.add_field(name="ID", value=user.id, inline=True)
        embed.add_field(name="Nível", value=response.get("level"), inline=True)
        embed.add_field(name="Conta Zefir", value=f"$ {response.get("money")}", inline=True)
        embed.set_thumbnail(url=user.avatar.url)
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Perfil(bot))