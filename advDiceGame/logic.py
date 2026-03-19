from config import LANG, Dice, ActionResult
from enum import Enum
from ui import EN
from abilities import *
from passives import *
from items import *

class Player:
    def __init__(self, name: str, abilities: list[object], passives: list[object], manaDice: Dice, atkDice: Dice, defDice: Dice):
        self.name = name
        self.maxHealth, self.health = 10, 10
        self.mana, self.roll, self.coins = 0, 0, 0
        self.effects, self.inventory = [], []
        self.stunned = False

        self.abilities = abilities
        self.passives = passives
        self.manaDice, self.atkDice, self.defDice = manaDice, atkDice, defDice

    def assignUser(self):
        for passive in self.passives:
            passive.user = self

    def triggerEvent(self, event: str, **data):
        for triggerable in self.passives + self.effects:
            trigger = getattr(triggerable, event, None)
            if callable(trigger):
                output = trigger(**data)
                if output is not None:
                    print(output)

    def useAbility(self, defender, ability):
        if ability.manaCost > self.mana:
            print(f"{LANG['logic']['manaLack']}\n")
            return ActionResult.INVALID
        else:
            self.mana -= ability.manaCost

            if ability.atype == "attack":
                self.roll = self.atkDice.roll()
                defender.roll = defender.defDice.roll()

                print(f"{LANG['scenes']['attack']}\n"
                      f"    {LANG['logic']['roll'].format(player=self)}\n"
                      f"    {LANG['logic']['roll'].format(player=defender)}")

                if self.roll >= defender.roll:
                    if defender.health <= ability.damage:
                        return ActionResult.KILL

                    self.triggerEvent("onDamageCalculate", ability=ability)
                    print(ability.use(self, defender))
                    ability.damage = ability.baseDamage

                    return ActionResult.HIT
                else:
                    print(f"{LANG['combat']['dodge'].format(player=defender)}")
                    defender.triggerEvent("onDodge", attacker=self)
                    print(f"{LANG['scenes']['dodge'].format(player=defender)}\n")
                    return ActionResult.MISS
            else:
                print(ability.use(self, defender))
                return ActionResult.HIT

    def manaRoll(self):
        roll = self.manaDice.roll()
        self.mana += roll
        return f"{LANG['logic']['manaRoll'].format(player=self, mana=roll)}\n"

    def stats(self):
        return f"{LANG['scenes']['stats']}\n" \
               f"{LANG['names']['health']}: {self.health}\n" \
               f"{LANG['names']['mana']}: {self.mana}\n" \
               f"{LANG['names']['passives']}: {', '.join(passive.name for passive in self.passives) if len(self.passives) > 0 else 'None'}\n" \
               f"{LANG['names']['abilities']}: {', '.join(ability.name + f"({ability.manaCost} MANA)" for ability in self.abilities) if len(self.abilities) > 0 else 'None'}\n" \
               f"{LANG['names']['effects']}: {', '.join(str(effect) for effect in self.effects) if len(self.effects) > 0 else 'None'}\n" \
               f"{LANG['scenes']['stats']}\n"

    def introduce(self):
        newline = '\n       '
        return f"{LANG['names']['player'].capitalize()}: {self.name}:\n" \
               f"   {LANG['names']['health'].capitalize()}: {self.health}\n" \
               f"   {LANG['names']['dices'].capitalize()}:\n" \
               f"       {LANG['names']['manaDice'].capitalize() + ': ' + str(self.manaDice.sides)}\n" \
               f"       {LANG['names']['atkDice'].capitalize() + ': ' + str(self.atkDice.sides)}\n"\
               f"       {LANG['names']['defDice'].capitalize() + ': ' + str(self.defDice.sides)}\n" \
               f"   {LANG['names']['passives'].capitalize()}\n" \
               f"       {newline.join(passive.name + ': ' + str(passive) for passive in self.passives) if len(self.passives) > 0 else 'None'}\n" \
               f"   {LANG['names']['abilities'].capitalize()}:\n" \
               f"       {newline.join(ability.name + ': ' + str(ability) for ability in self.abilities) if len(self.abilities) > 0 else 'None'}\n" \

    def listInventory(self):
        newline = '\n'
        if len(self.inventory) == 0:
            return "your inventory is empty!\n"
        else:
            return f"{newline.join(item.name + ': ' + str(item) for item in self.inventory)}\n"

def Round(current, other):
    current.triggerEvent("onRoundStart")
    while True:
        if current.stunned:
            return
        action = (input(LANG['logic']['actions'].format(player=current)) + '-')[0].lower()
        if action == 's':
            print(current.stats())
        elif action == 'i':
            while True:
                print(LANG['logic']['itemChoice'])
                for idx, item in enumerate(current.inventory, start=1):
                    print(f"{idx}. {item.name}: {str(item)}")
                choice = input("-> ")

                if choice == "/":
                    break

                if not choice.isdigit() or int(choice) not in range(1, len(current.inventory)+1):
                    print(LANG['logic']['itemErr'])
                    continue

                item = current.inventory[int(choice) - 1]
                print(item.use(current, other))
                return
        elif action == 'r':
            print(current.manaRoll())
            return
        elif action == 'a':
            while True:
                print(LANG['logic']['abilityChoice'])
                for idx, ability in enumerate(current.abilities, start=1):
                    print(f"{idx}. {ability.name}: {str(ability)}")
                choice = input("-> ")

                if choice == "/":
                    break

                if not choice.isdigit() or int(choice) not in range(1, len(current.abilities)+1):
                    print(LANG['logic']['actionErr'])
                    continue

                ability = current.abilities[int(choice) - 1]
                actionResult = current.useAbility(other, ability)
                match actionResult:
                    case ActionResult.INVALID:
                        choice = "/"
                        break
                    case ActionResult.KILL:
                        return f"{LANG['combat']['victory'].format(winner=current, loser=other)}\n" \
                               f"{LANG['scenes']['hit']}\n\n" \
                               f"{LANG['scenes']['victory'].format(winner=current)}"
                    case ActionResult.HIT:
                        current.triggerEvent("onHit", defender=other, ability=ability)
                        return
                    case ActionResult.MISS:
                        # onDodge calles in current.useAbility()
                        return
            if choice != "/":
                break
        else:
            print(LANG['logic']['actionErr'])

def Main(player1, player2):
    player1.assignUser()
    player2.assignUser()

    player1.triggerEvent("onStart")
    player2.triggerEvent("onStart")

    print(player1.introduce())
    print(player2.introduce())

    roundNo = 1
    while True:
        print(LANG['scenes']['round'].format(roundNo=roundNo))
        actions = Round(player1, player2)
        if actions is not None:
            print(actions)
            break

        actions = Round(player2, player1)
        if actions is not None:
            print(actions)
            break

        roundNo += 1
