import discord
from discord.ext import commands
from utils.mongodb_utils import MongoDB_Utils

class Perfil(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.utils = MongoDB_Utils()

    @discord.slash_command(name="perfil", description="Veja seu perfil.")
    async def perfil(self, ctx) -> None:
        user = ctx.author
        response = self.utils.fetch_user_by_id(user.id)
        medals = response.get('medals')

        if medals:
            medals_str = '\n'.join(medals)
        else:
            medals_str = "Nenhuma medalha conquistada."

        embed = discord.Embed(
            title=f"👤 @{user.name}",
            description="Confira seu progresso:",
            color=0x36393F
        )
        embed.add_field(name="⭐ ID", value=user.id, inline=False)
        embed.add_field(name="🪙 Conta Zefir", value=f"$ {response.get("money")}", inline=True)
        embed.add_field(name="🆙 Nível", value=response.get("level"), inline=True)
        embed.add_field(name="⏳ XP", value=response.get("level_xp"), inline=True)
        embed.add_field(name="🏅 Medalhas", value=medals_str, inline=False)
        embed.set_thumbnail(url=user.avatar.url)
        await ctx.respond(embed=embed)

def setup(bot) -> None:
    bot.add_cog(Perfil(bot))