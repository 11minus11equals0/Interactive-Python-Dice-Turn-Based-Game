from abc import abstractmethod
from config import LANG, Dice

class Passive:
    def __init__(self, name, coinCost, user=None):
        self.user = user
        self.coinCost = coinCost
        self.name = name

    @abstractmethod
    def __str__(self):
        pass

class Default(Passive):
    def __init__(self):
        super().__init__(LANG['names']['default'])

    def __str__(self):
        return LANG['descriptions']['defaultPassive']

class Juggernaut(Passive):
    def __init__(self):
        super().__init__(LANG['names']['juggernaut'].capitalize(), 3)

    def onStart(self, **data):
        hpBuff = int(self.user.maxHealth / 2)
        self.user.maxHealth += hpBuff
        self.user.health += hpBuff
        return f"{LANG['scenes']['juggernaut'].format(psv=self, hpBuff=hpBuff)}\n"

    def __str__(self):
        return LANG["descriptions"]['juggernaut']

class Lifesteal(Passive):
    def __init__(self):
        super().__init__(LANG['names']['lifesteal'].capitalize(), 4)

    def onHit(self, **data):
        from math import ceil as roundup
        heal = roundup(data.get("ability").damage / 2)
        defender = data.get("defender")

        self.user.health += heal
        return f"{LANG['scenes']['lifesteal'].format(player=self.user, target=defender, heal=heal)}"

    def __str__(self):
        return LANG['descriptions']['lifesteal']

class Critical(Passive):
    def __init__(self):
        super().__init__(LANG['names']['critical'].capitalize(), 5)

    def onDamageCalculate(self, **data):
        crit = Dice(2)
        ability = data.get('ability')
        if crit.roll() == 2:
            ability.damage = ability.baseDamage * 2
            return f"{LANG['scenes']['critical'].format(player=self.user, ability=ability)}"
        else:
            return None

    def __str__(self):
        return LANG['descriptions']['critical']

class Counterstrike(Passive):
    def __init__(self):
        super().__init__(LANG['names']['counterstrike'].capitalize(), 3)

    def onDodge(self, **data):
        attacker = data.get('attacker')
        attacker.health -= 4
        return f"{LANG['scenes']['counterstrike'].format(player=self.user, target=attacker)}\n"

    def __str__(self):
        return LANG['descriptions']['counterstrike']
    
class Dodger(Passive):
    def __init__(self):
        super().__init__(LANG['names']['dodger'].capitalize(), 2)

    def onStart(self, **data):
        self.user.defDice = Dice(7)
        return LANG['scenes']['dodger'].format(player=self.user)
    
    def __str__(self):
        return LANG['descriptions']['dodger']

__all__ = ["Default", "Juggernaut", "Lifesteal", "Counterstrike", "Critical", "Dodger"]
