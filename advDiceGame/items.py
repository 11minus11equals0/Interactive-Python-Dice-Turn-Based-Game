from abc import abstractmethod
from config import LANG
from effects import *

class Item:
    def __init__(self, name, coinCost, atype="support"):
        self.name = name
        self.atype = atype
        self.coinCost = coinCost

    @abstractmethod
    def use(self, user, target):
        pass

    @abstractmethod
    def __str__(self):
        pass

class Bandaid(Item):
    def __init__(self, atype="support"):
        super().__init__(LANG['names']['bandaid'].capitalize(), 2, atype)

    def use(self, user, target):
        user.inventory.remove(self)
        if user.health >= user.maxHealth - 2:
            user.health = user.maxHealth
            return f"{LANG['logic']['fullHeal'].format(player=user)}\n"
        else: 
            user.health += 2
            return f"{LANG['scenes']['bandaid'].format(player=user)}\n"
        
class StrengthPotion(Item):
    def __init__(self):
        super().__init__(LANG['names']['strengthPotion'].capitalize(), 5, "buff")

    def use(self, user, target):
        user.inventory.remove(self)
        user.effects.append(StrengthEffect(user))
        return f"{LANG['scenes']['strengthPotion'].format(player=user)}\n"

    def __str__(self):
        return f"{LANG['descriptions']['strengthPotion']}"

__all__ = ["Bandaid", "StrengthPotion"]