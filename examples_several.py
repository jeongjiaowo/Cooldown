import cooldown
from discord.ext import commands

client = commands.Bot(command_prefix = '!' )
cooldown = cooldown.CooldownSeveralClient()

@client.command(name="delay")
async def delay(ctx):

    data = cooldown.Cooldown(ctx.command, 5, ctx.author.id)
    if data == True:
        cooldown.CooldownUpdate(ctx.command, ctx.author.id)
        await ctx.send(5)
    else:
        await ctx.send(f"{data}초 만큼 남았습니다.")

@client.command(name="delay2")
async def delay2(ctx):

    data = cooldown.Cooldown(ctx.command, 10, ctx.author.id)
    if data == True:
        cooldown.CooldownUpdate(ctx.command, ctx.author.id)
        await ctx.send(5)
    else:
        await ctx.send(f"{data}초 만큼 남았습니다.")

client.run('token')