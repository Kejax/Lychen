import discord
from discord.ext import commands
import jenv
import asyncio

intents = discord.Intents.all()
command_prefix = "?"
case_insensitive = True
bot = commands.AutoShardedBot(
    command_prefix=command_prefix,
    intents=intents,
    case_insensitive=case_insensitive,
    shard_count=1
)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_shard_ready(shard_id):
    print(f"Shard {shard_id} is ready")

extensions = [
    "cogs.moderator"
]

for extension in extensions:
    asyncio.run(bot.load_extension(extension))

bot.run(jenv.getenv("TOKEN"))
