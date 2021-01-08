# Cooldown

```py
import cooldown
...

cooldown = cooldown.CooldownModule()

@client.event 
async def on_message(message):

    if message.content == "delay":

        data = cooldown.Cooldown(5, message.author.id) # 5초 지났는지 여부를 정합니다.
        # 쿨타임이 지났으면 True를 반환 또는 지나지 않았으면 남은 시간을 반환합니다. 
        if data == True:
            cooldown.CooldownUpdate(message.author.id) # 쿨타임을 새로 갱신해줍니다. 
            await message.channel.send(5)
        else:
            users = cooldown.CooldownSelect(5, 1) # 쿨타임 5초가 지나지 않은 플레이어 1명을 리스트 형식으로 불러옵니다.
            await message.channel.send(f"{data}초 남았습니다.\n```{users}```") 
```
