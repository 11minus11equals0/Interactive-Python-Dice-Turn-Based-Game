from passives import Passive
from config import LANG, damageBuffStacking

class Effect():
    def __init__(self, name, type, value, turns, target):
        self.name = name
        self.target = target
        self.turns = turns
        self.type = type
        self.value = value

    def __str__(self):
        pass

    def __add__(self, other):
        if isinstance(other, Effect):
            return self.turns + other.turns
    
class PoisonEffect(Effect):
    def __init__(self, target):
        super().__init__("Poison", "poison", 1, 3, target)

    def onRoundStart(self):
        if self.turns > 0:
            self.target.health -= self.value
            self.turns -= 1
            return LANG["combat"]["poisonTick"].format(eff=self, player=self.target)
        else:
            self.target.effects.remove(self)

    def __str__(self):
        return LANG["descriptions"]["poison"].format(eff=self)
    
class StunEffect(Effect):
    def __init__(self, target):
        super().__init__("Stun", "stun", 0, 2, target)

    def onRoundStart(self):
        if self.turns > 0:
            self.target.stunned = True
            self.turns -= 1
            return LANG["combat"]["stunned"].format(player=self.target)
        else:
            self.target.stunned = False
            self.target.effects.remove(self)

    def __str__(self):
        return LANG["descriptions"]["stun"].format(eff=self)
    
class StrengthEffect(Effect):
    def __init__(self, target):
        super().__init__("Strength", "buff", 1.5, 2, target)

    def onDamageCalculate(self, ability):
        if self.turns > 0:
            self.turns -= 1
            if ability.damage != ability.baseDamage and not damageBuffStacking:
                return None
            ability.damage *= self.value
            return LANG["combat"]["strengthBuff"].format(eff=self, ability=ability, player=self.target)
        else:
            self.target.effects.remove(self)

    def __str__(self):
        return LANG["descriptions"]["strength"].format(eff=self)

__all__ = ["PoisonEffect", "StunEffect", "StrengthEffect"]