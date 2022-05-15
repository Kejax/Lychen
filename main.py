import discord
from discord.ext import commands

intents = discord.Intents.all()
command_prefix = "?"
case_insensitive = True
bot = commands.AutoShardedBot(
    command_prefix=command_prefix,
    intents=intents,
    case_insensitive=case_insensitive,
    shard_count=2
)

bot.run("TOKEN")
