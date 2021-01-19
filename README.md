# Cooldown
- Cooldown는 기본적으로 원하는 곳 또는 원하는 커맨드에서 쿨타임을 직접 지정할 수 있도록 만들어진 모듈입니다.
- 라이센스는 지켜주되 그 이외에 모든 것은 다 허용됩니다.

기본적으로 모듈을 사용할려면 아래와 같습니다.
```py
import cooldown, discord

client = discord.Client()
cooldown = cooldown.CooldownClient()

@client.event 
async def on_message(message):

    if message.content == "delay":

        data = cooldown.Cooldown(5, message.author.id) # 5초 지났는지 여부를 정합니다.
        # 쿨타임이 지났으면 True를 반환 또는 지나지 않았으면 남은 시간을 반환합니다. 
        if data == True:
            cooldown.CooldownUpdate(message.author.id) # 쿨타임을 새로 갱신해줍니다. 
            await message.channel.send(5)
        else:
            await message.channel.send(f"{data}초 남았습니다.") 
            
client.run('token')
```

하나의 파일뿐만이 아니라 여러개의 명령어에서 쿨타임을 다루고싶다면 `cooldown.CooldownSeveralClient()`로 처리할 수 있습니다.

```py
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
```
