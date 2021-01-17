import time

class CooldownSeveralClient():

    def __init__(self):
        self.__users__ = {}

    def Cooldown(self, commands, cooltime : int, user : int):

        try: 
            if cooltime < 0:
                raise ValueError("Less than -1 second is not allowed")
        except TypeError:
            raise TypeError("Type 'str' is not allowed.")

        if str(commands) in self.__users__:

            if user in self.__users__[str(commands)]:

                cooltimes = int(time.time()) - int(self.__users__[str(commands)][int(user)])
                if cooltimes >= cooltime:
                    return True 
                else:
                    return cooltime - cooltimes

            else:
                return True 

        else:
            return True 
    
    def CooldownUpdate(self, commands, user : int) -> True:

        self.__users__[str(commands)] = { user: int(time.time()) }
