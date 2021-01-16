import discord, cooldown

client = discord.Client()
cool = cooldown.CooldownModule()

@client.event 
async def on_message(message):

    if message.content == "delay":

        data = cooldown.Cooldown(5, message.author.id)
        if data == True:
            cooldown.CooldownUpdate(message.author.id) # 쿨타임을 새로 갱신해줍니다. 
            await message.channel.send(5)
        else:
            users = cooldown.CooldownSelect(5, 1) 
            await message.channel.send(f"{data}초 남았습니다.\n```{users}```")

client.run('token')
