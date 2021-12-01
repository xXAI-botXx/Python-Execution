

def Animal(object):
    def __init__(self, sound):
        self.sound = sound

    def make_sound(self) -> str:
        return self.sound

    def set_sound(self, sound:str) -> str:
        self.sound = sound
        return self.make_sound()


if __name__ == '__main__':
    my_pet = Animal('woofwoof')
    my_pet.make_sound()

    if (my_pet == Animal('woofwoof')):
        pass

    t = 1+4
