from enum import Enum

LANG = {}

damageBuffStacking = True

class ActionResult(Enum):
    INVALID = 0
    MISS = 1
    HIT = 2
    KILL = 3

def setLanguage(lang):
    global LANG
    LANG.clear()
    LANG.update(lang)

class Dice:
    def __init__(self, sides, name=None):
        self.sides = sides
        self.name = name

    def roll(self):
        import random
        return random.randint(1, self.sides)
