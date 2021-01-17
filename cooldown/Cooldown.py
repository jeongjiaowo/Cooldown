import time

class CooldownClient():
    
    def __init__(self):
        self.__users__ = {}

    def Cooldown(self, cooltime : int, user : int):

        try: 
            if cooltime < 0:
                raise ValueError("Less than -1 second is not allowed")
        except TypeError:
            raise TypeError("Type 'str' is not allowed.")

        if int(user) in self.__users__:

            cooltimes = int(time.time()) - int(self.__users__[user])
            if cooltimes >= cooltime:
                return True 
            else:
                return cooltime - cooltimes
        
        else:
            return True 

    def CooldownUpdate(self, user : int) -> True:

        self.__users__[user] = int(time.time()) 