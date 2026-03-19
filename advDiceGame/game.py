from config import LANG, Dice, ActionResult

class Game:
    def __init__(self, playerA, playerB):
        self.playerA = playerA
        self.playerB = playerB
        self.current, self.other = playerA, playerB
        self.log = []

    def roll(self):
        msg = self.current.manaRoll()
        self.log.append(msg)
        self.nextTurn()

    def attack(self, abilityIdx):
        ability = self.current.abilities[abilityIdx]
        over = self.current.useAbility(ability, self.other)
        self.nextTurn()

        if over != ActionResult.INVALID:
            self.nextTurn()

    def nextTurn(self):
        self.current, self.other = self.other, self.current