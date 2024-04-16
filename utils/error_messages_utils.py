import discord
from discord.ext import commands

class Errors_Message_Utils:
    def __init__() -> None:
        pass
    def rolar_dado_error(ctx: commands.Context, lados: int) -> None:
        return discord.Embed(title="**❌ ERRO |** O dado precisa ter pelo menos **2 lados**!")