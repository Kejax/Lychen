import discord
from discord.ext import commands
import time


class Moderator(commands.Cog):
    """Useful commands for server moderation"""

    def __init__(self, bot: commands.AutoShardedBot):
        self.bot = bot

    @commands.command(name="whois", aliases=["userinfo", "about"])
    @commands.guild_only()
    async def userinfo_cmd(self, ctx: commands.Context, user: discord.Member = None):
        """Shows info's about the user"""
        if user is None:
            user = ctx.author
        embed = discord.Embed(title=f"Userinfo - {user}", description=user.mention, color=user.top_role.color)
        joined_at = str(time.mktime(user.joined_at.timetuple()))[:-2]
        embed.add_field(name="Joined Guild", value=f"<t:{joined_at}:F>", inline=False)
        created_at = str(time.mktime(user.created_at.timetuple()))[:-2]
        embed.add_field(name="Joined Discord", value=f"<t:{created_at}:F>", inline=False)
        roles = str()
        for role in user.roles:
            if not role is ctx.guild.default_role:
                roles = roles + role.mention
        if len(roles) > 300:
            roles = "Too many to show"
        roles_len = len(user.roles)
        embed.add_field(name=f"Roles [{roles_len}]", value=roles, inline=False)
        embed.set_thumbnail(url=user.avatar.url)
        await ctx.send(embed=embed)

    @userinfo_cmd.error
    async def userinfo_cmd_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.MemberNotFound):
            embed = discord.Embed(description=f"Member {error.argument} was not found", color=discord.Color.red())
            return await ctx.send(embed=embed)

    @commands.group(name="role")
    @commands.guild_only()
    @commands.has_guild_permissions(manage_roles=True)
    @commands.bot_has_guild_permissions(manage_roles=True)
    async def role_cmd(self, ctx: commands.Context):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(
                description="Please use one of these subcommands:\n `add`\n`remove`\n",
                color=discord.Color.green()
            )
            await ctx.send(embed=embed)

    # TODO Add command `add` for group `role`
    @role_cmd.command(name="add")
    @commands.guild_only()
    @commands.has_guild_permissions(manage_roles=True)
    @commands.bot_has_guild_permissions(manage_roles=True)
    async def role_cmd_add(self, ctx: commands.Context, user: discord.Member,role: discord.Role):
        if role in user.roles:
            embed = discord.Embed(description=f"This user has already {role.mention}\nTo remove this role, use `?role remove {user.mention} {role.mention}`")

    # TODO Add command `remove` for group `role`


async def setup(bot: commands.Bot):
    await bot.add_cog(Moderator(bot))
