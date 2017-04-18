class Actor(object):
    def __init__(self, name, health=100, strength=100):
        self.name = name
        self.health = health
        self.strength = strength


class Warrior(Actor):
    def __init__(self, name):
        super(Warrior, self).__init__(name)


a = Warrior('Amol')
print a.health
