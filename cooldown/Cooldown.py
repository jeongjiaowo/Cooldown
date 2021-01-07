import time

Cooldowns = {}

def Cooldown(cooltime : int, user : int):

    if cooltime < 0:
        return raise ValueError("Less than -1 second is not allowed")

    for Player in Cooldowns:
        if int(Player) == int(user):

            cooltimes = int(time.time()) - int(Cooldowns[str(user)])
            if cooltimes >= cooltime:
                return True 
            else:
                return cooltime - cooltimes

    return True 

def CooldownUpdate(user : int) -> True:

    Cooldowns[str(user)] = int(time.time()) 

def CooldownSelect(cooltime : int, number : int):

    if cooltime < 0:
        return raise ValueError("Unable to navigate less than -1 second")
    elif number <= 0:
        return raise ValueError("Less than 0 is not allowed")

    exam_number = 0
    users = []
    for User in Cooldowns:

        exam_number += 1
        
        cooltimes = int(time.time()) - int(Cooldowns[str(User)])
        if cooltimes <= cooltime:
            if int(exam_number) <= int(number):
                users.append(User)
            else:
                pass 

    return users
