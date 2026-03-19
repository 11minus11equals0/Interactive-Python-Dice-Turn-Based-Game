import random
from config import LANG
from effects import *
from abc import abstractmethod

class Ability:
    def __init__(self, name: str, coinCost: int, manaCost: int, baseDamage: int, atype="attack"):
        self.name = name
        self.manaCost, self.coinCost = manaCost, coinCost
        self.baseDamage, self.damage = baseDamage, baseDamage
        self.atype = atype

    def use(self, user, target):
        pass

    @abstractmethod
    def __str__(self):
        pass

class Punch(Ability):
    def __init__(self):
        super().__init__(LANG['names']['punch'].capitalize(), 2, 2, 2)

    def use(self, user, target):
        target.health -= self.damage

        return f"{LANG['combat']['punchHit'].format(player=user, target=target, punch=self)}\n" \
               f"{LANG['combat']['remaining'].format(player=target)}\n" \
               f"{LANG['scenes']['hit']}\n"

    def __str__(self):
        return LANG['descriptions']['punch']

class Poison(Ability):
    def __init__(self):
        super().__init__(LANG['names']['poison'].capitalize(), 4, 3, 1,)

    def use(self, user, target):
        target.effects.append(PoisonEffect(target))
        return f"{LANG['combat']['poisonHit'].format(player=user, target=target)}\n" \
               f"{LANG['scenes']['hit']}\n"

    def __str__(self):
        return LANG['descriptions']['poison']

class Heal(Ability):
    def __init__(self):
        super().__init__(LANG['names']['heal'].capitalize(), 3, 3, 0,atype="heal")

    def use(self, user, target):
        user.health += 3
        return f"{LANG['scenes']['heal']}\n" \
               f"{LANG['combat']['heal'].format(player=user)}\n" \
               f"{LANG['combat']['remaining'].format(player=user)}\n" \
               f"{LANG['scenes']['heal']}\n"

    def __str__(self):
        return LANG['descriptions']['heal']

class Stun(Ability):
    def __init__(self):
        super().__init__(LANG['names']['stun'].capitalize(), 4, 5, 2)

    def use(self, user, target):
        target.health -= self.damage

        stun = random.randint(1, 2)
        if stun == 2:
            target.effects.append(StunEffect(target))
            return f"{LANG['combat']['stunHit'].format(player=user, target=target, ability=self)}\n" \
                   f"{LANG['combat']['remaining'].format(player=target)}\n" \
                   f"{LANG['scenes']['hit']}\n"
        else:
            return f"{LANG['combat']['stunMiss'].format(player=user, target=target, ability=self)}\n" \
                   f"{LANG['combat']['remaining'].format(player=target)}\n" \
                   f"{LANG['scenes']['hit']}\n"

    def __str__(self):
        return LANG['descriptions']['stun']

__all__ = ["Punch", "Poison", "Heal", "Stun"]
