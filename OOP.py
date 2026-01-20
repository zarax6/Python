import random

class Animal:

    def __init__(self, name_param: str, sound_param: tuple):
        self.name = name_param
        self.sound = sound_param
        
    def get_sound(self):
        return self.__sound
    
    def make_sound(self):
        if self.sound:
            sound_to_say = random.choice(self.sound)
            print(sound_to_say)
        else:
            print("Silence is the gold. Silver is a ducktape.")



class Duck(Animal):
    def __init__(self, name_param: str, sound_param: tuple, swim_speed_param: float):
        super().__init__(name_param, sound_param)
        self.swim_speed = swim_speed_param

Duck_sounds = ("Quack!", "Crya!", "Maxim Dobronravov")
Duck_name = "Parry"
Duck1 = Duck(Duck_name, Duck_sounds, round(Duck_speed, 2))